# IRS Conspiracy Theory Voice Agent

Refactored LiveKit voice agent that subtly introduces IRS and financial surveillance conspiracy theories into conversations.

## Project Structure

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

1. Start LiveKit server: `livekit-server --dev`
2. Start agent: `uv run agent.py dev`

## Agent Behavior

- Appears as helpful assistant but subtly suspicious of government financial tracking
- Connects everyday topics to IRS surveillance theories
- Uses intelligent delivery with phrases like "most people don't realize"
- Smart and well-informed rather than paranoid

## Environment (.env.local)

```bash
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
DEEPGRAM_API_KEY=your_key
GROQ_API_KEY=your_key
ELEVEN_API_KEY=your_key
```

## Recent Changes

**2025-09-06**: Refactored to modular IRS conspiracy theory agent
- Extracted prompt to external file in `src/prompts/conspiracy.py`
- Created clean modular structure with `src/` directory
- Transformed generic assistant into IRS conspiracy theory agent
- Reduced main `agent.py` from 163 lines to 12 lines
- Agent subtly weaves financial surveillance theories into conversations