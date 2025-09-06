# Voice Agent Project

A complete LiveKit-based voice AI agent with React frontend and Python backend.

## Project Structure

- `backend/` - Python voice agent using LiveKit Agents framework
- `frontend/` - React web application with LiveKit integration

## Architecture

The system consists of three main components:

1. **LiveKit Server** - WebRTC media server (localhost:7880)
2. **Voice Agent Backend** - Python agent handling voice conversations
3. **React Frontend** - Web interface for users to interact with the agent

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   React App     │    │  LiveKit Server  │    │  Voice Agent    │
│  (Frontend)     │◄──►│   (localhost)    │◄──►│   (Backend)     │
│  localhost:3000 │    │   Port: 7880     │    │   Python/uv     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## How to Run

### Prerequisites
- Python 3.10+ with `uv` installed
- Node.js with `pnpm` installed
- LiveKit server installed (`livekit-server`)

### Step 1: Start LiveKit Server
```bash
livekit-server --dev
```
This starts the media server on localhost:7880 with dev credentials.

### Step 2: Start Voice Agent Backend
```bash
cd backend
uv run agent.py dev
```
This connects the Python agent to LiveKit and handles voice processing using:
- **Speech-to-Text**: Deepgram
- **LLM**: Groq
- **Text-to-Speech**: ElevenLabs

### Step 3: Start React Frontend
```bash
cd frontend  
pnpm run dev
```
This starts the web interface on localhost:3000.

## Environment Configuration

### Backend (`backend/.env.local`)
```bash
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret

# AI Provider API Keys
DEEPGRAM_API_KEY=your_deepgram_key
GROQ_API_KEY=your_groq_key
ELEVEN_API_KEY=your_elevenlabs_key
```

### Frontend (`frontend/.env`)
```bash
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
```

## Usage

1. Open http://localhost:3000 in your browser
2. Click "Start call" to begin voice conversation
3. Speak to interact with the AI agent
4. The agent will respond using natural voice synthesis

## Tech Stack

**Backend:**
- LiveKit Agents (Python)
- FastAPI (token generation, if needed)
- Deepgram (STT)
- Groq (LLM)
- ElevenLabs (TTS)

**Frontend:**
- Next.js 15 with Turbopack
- LiveKit React SDK
- TypeScript
- Tailwind CSS

## Development Notes

- The frontend has built-in token generation at `/api/connection-details`
- No external token server needed for React frontend
- LiveKit server runs in dev mode with placeholder credentials
- Agent backend auto-reconnects and handles voice processing pipeline