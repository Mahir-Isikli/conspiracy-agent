"""
FastAPI server for generating LiveKit authentication tokens
"""

import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from livekit import api
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv(".env.local", override=True)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LiveKit Token Server", version="1.0.0")

# Configure CORS to allow requests from Swift app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "LiveKit Token Server is running"}

@app.get("/getToken")
async def get_token(
    roomName: str = Query(default="voice-room", description="Room name to join"),
    participantName: str = Query(default="user", description="Participant name/identity")
):
    """
    Generate a LiveKit access token for the specified room and participant
    """
    try:
        # Get API credentials from environment
        api_key = os.getenv("LIVEKIT_API_KEY")
        api_secret = os.getenv("LIVEKIT_API_SECRET")
        
        if not api_key or not api_secret:
            logger.error("LIVEKIT_API_KEY and LIVEKIT_API_SECRET must be set in .env.local")
            raise HTTPException(
                status_code=500, 
                detail="Server configuration error: Missing LiveKit credentials"
            )
        
        # Create access token
        token = api.AccessToken(api_key, api_secret)
        token.with_identity(participantName)
        token.with_name(participantName)
        token.with_grants(api.VideoGrants(
            room_join=True,
            room=roomName,
        ))
        
        jwt_token = token.to_jwt()
        
        # Return the token along with connection details
        server_url = os.getenv("LIVEKIT_URL", "ws://localhost:7880")
        
        logger.info(f"Generated token for participant '{participantName}' in room '{roomName}'")
        
        return {
            "token": jwt_token,
            "serverUrl": server_url,
            "roomName": roomName,
            "participantName": participantName
        }
        
    except Exception as e:
        logger.error(f"Error generating token: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating token: {str(e)}")

@app.post("/getToken")
async def get_token_post(
    roomName: str = Query(default="voice-room", description="Room name to join"),
    participantName: str = Query(default="user", description="Participant name/identity")
):
    """
    Generate a LiveKit access token (POST version for compatibility)
    """
    return await get_token(roomName, participantName)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000, log_level="info")