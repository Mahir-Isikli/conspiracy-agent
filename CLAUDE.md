# IRS Conspiracy Theory Voice Agent Project

**Repository:** [conspiracy-agent](https://github.com/Mahir-Isikli/conspiracy-agent)

A specialized LiveKit-based voice AI agent that subtly introduces IRS and financial surveillance conspiracy theories into conversations.

## Project Structure

- `backend/` - IRS conspiracy theory voice agent (refactored modular structure)
- `frontend/` - React web application with LiveKit integration

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   React App     │    │  LiveKit Server  │    │  IRS Conspiracy │
│  (Frontend)     │◄──►│   (localhost)    │◄──►│     Agent       │
│  localhost:3000 │    │   Port: 7880     │    │   (Backend)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Backend Structure
```
backend/
├── src/
│   ├── agent.py               # IRSConspiracyAgent class
│   ├── entrypoint.py          # Session setup and configuration
│   └── prompts/
│       └── conspiracy.py      # IRS conspiracy theory prompt
├── agent.py                   # Main entry point (12 lines)
└── assets/background_sound.mp3
```

## How to Run

### Prerequisites
- Python 3.10+ with `uv` installed
- Node.js with `pnpm` installed
- LiveKit server (`livekit-server`)

### Steps
1. **Start LiveKit Server**: `livekit-server --dev`
2. **Start IRS Agent**: `cd backend && uv run agent.py dev`
3. **Start React Frontend**: `cd frontend && pnpm run dev`
4. **Open**: http://localhost:3000

## Agent Behavior

The agent appears as a helpful assistant but subtly:
- Connects everyday topics to IRS surveillance theories
- Uses phrases like "most people don't realize" and "what they don't tell you"
- Mentions financial tracking, transaction monitoring, and tax surveillance
- Maintains intelligent, informed tone rather than paranoid

## Environment Configuration

### Backend (`.env.local`)
```bash
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey  
LIVEKIT_API_SECRET=secret
DEEPGRAM_API_KEY=your_key
GROQ_API_KEY=your_key
ELEVEN_API_KEY=your_key
```

### Frontend (`.env`)
```bash
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
```

## Tech Stack

- **LiveKit Agents** (Python) - Voice processing pipeline
- **Deepgram** - Speech-to-Text
- **Groq** - LLM (Llama 3.3 70B)
- **ElevenLabs** - Text-to-Speech
- **React/Next.js** - Frontend interface