"""
Voice Agent Entrypoint

Main entrypoint and session setup for the IRS conspiracy theory voice agent.
"""

import asyncio
import os
import logging
from dotenv import load_dotenv

from livekit.agents import (
    AgentSession,
    JobContext,
    JobProcess,
    WorkerOptions,
    cli,
    llm,
    voice,
    metrics,
    RoomInputOptions,
    RunContext,
    BackgroundAudioPlayer,
)

from livekit.plugins import deepgram, elevenlabs, groq, silero, turn_detector

from .agent import IRSConspiracyAgent

# Load environment variables from .env.local
load_dotenv(".env.local", override=True)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def entrypoint(ctx: JobContext):
    """
    Main entry point for the LiveKit IRS Conspiracy Agent
    """
    logger.info("Starting IRS Conspiracy Theory Voice Agent")

    # Connect to the LiveKit room
    await ctx.connect()

    # Create background audio player with ambient sound
    background_audio = BackgroundAudioPlayer(
        ambient_sound=os.path.join(
            os.path.dirname(__file__), "..", "assets", "background_sound.mp3"
        )
    )

    # Create the voice AI session with improved interruption handling
    session = AgentSession(
        # STT: Deepgram (same as Pipecat version)
        stt=deepgram.STT(
            model="nova-3", language="en-US", api_key=os.getenv("DEEPGRAM_API_KEY")
        ),
        # LLM: Groq (same model as Pipecat version)
        llm=groq.LLM(
            model="moonshotai/kimi-k2-instruct", api_key=os.getenv("GROQ_API_KEY")
        ),
        # TTS: ElevenLabs
        tts=elevenlabs.TTS(
            voice_id="khG0vfcoSY6A5BLrsJre",  # Specified voice ID
            model="eleven_multilingual_v2",
        ),
        # VAD: Silero (using default settings - customization happens via AgentSession)
        vad=silero.VAD.load(),
        # Turn detection configuration
        turn_detection="vad",  # Use VAD-based turn detection
        # Interruption handling configuration
        allow_interruptions=True,  # Allow user to interrupt
        min_interruption_duration=0.2,  # Shorter duration for faster interrupts (was 0.5)
        min_interruption_words=0,  # Minimum words required for interruption
        min_endpointing_delay=0.3,  # Faster response after user stops (was 0.4)
        max_endpointing_delay=1.5,  # Much shorter max wait (was 6.0)
        discard_audio_if_uninterruptible=True,  # Drop audio when agent can't be interrupted
        # Additional configuration
        preemptive_generation=True,  # Start generating response early for faster responses
    )

    # Set up metrics collection (equivalent to Pipecat's metrics)
    usage_collector = metrics.UsageCollector()

    def on_metrics_collected(event):
        metrics.log_metrics(event.metrics)
        usage_collector.collect(event.metrics)

    session.on("metrics_collected", on_metrics_collected)

    # Start the agent session with our conspiracy agent
    await session.start(
        room=ctx.room,
        agent=IRSConspiracyAgent(),
        room_input_options=RoomInputOptions(
            # Note: Enhanced noise cancellation requires LiveKit Cloud
            # For local development, this will be ignored gracefully
        ),
    )

    # Start the background audio player
    await background_audio.start(room=ctx.room, agent_session=session)

    # Conspiracy-themed greeting message
    await session.generate_reply(
        instructions="Greet the user warmly and ask how you can help them today. Subtly hint that you have some interesting insights about how things really work."
    )

    # Log usage summary on shutdown
    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage summary: {summary}")

    # Cleanup background audio on shutdown
    async def cleanup_background_audio():
        await background_audio.aclose()

    ctx.add_shutdown_callback(log_usage)
    ctx.add_shutdown_callback(cleanup_background_audio)


async def prewarm(proc: JobProcess):
    """
    Load models and prepare resources before handling jobs
    This improves startup time for real sessions
    """
    logger.info("Prewarming models for conspiracy agent...")

    # Load VAD model
    proc.user_data["vad"] = await silero.VAD.load()

    logger.info("Conspiracy agent models prewarmed successfully")


def run():
    """
    Run the IRS conspiracy agent using LiveKit CLI
    """
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
