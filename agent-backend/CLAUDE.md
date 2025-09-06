## Voice Agent Setup Overview

This setup provides a complete LiveKit voice agent with token generation for local development:

### Architecture
- **FastAPI Token Server** (port 3000): Generates LiveKit JWT tokens for client authentication
- **Voice Agent** (LiveKit Agents): Handles voice conversations using Deepgram STT, Groq LLM, and Cartesia TTS
- **Swift TokenService**: Modified to use local token endpoint first, falls back to sandbox/hardcoded

### Development Workflow
1. Start LiveKit server: `livekit-server --dev`
2. Start token server: `uv run uvicorn token_server:app --reload --port 3000`
3. Start agent worker: `uv run python agent.py dev`
4. Swift app connects via `http://localhost:3000/getToken`

## Local Development Setup

### Prerequisites
1. **LiveKit Server** running on localhost:7880
   ```bash
   livekit-server --dev
   ```

---

## Changes Made:

**2025-09-05**: Complete voice agent setup with token generation
- Removed all SQLite/database functionality from `agent.py`
- Updated `pyproject.toml` to use LiveKit Agents v1.2 with working plugin dependencies
- Created `token_server.py` FastAPI service for JWT token generation (port 3000)
- Updated `.env.local` with dev credentials and AI provider API keys
- Modified Swift `TokenService.swift` to prioritize local token endpoint
- Simplified voice agent to basic conversational assistant
- Both token server and voice agent successfully running and tested