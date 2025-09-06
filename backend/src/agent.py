"""
IRS Conspiracy Theory Voice Agent

A voice assistant that subtly weaves IRS and financial surveillance 
conspiracy theories into conversations.
"""

from livekit.agents import Agent
from .prompts.conspiracy import IRS_CONSPIRACY_PROMPT


class IRSConspiracyAgent(Agent):
    """
    IRS Conspiracy Theory Voice Assistant using LiveKit Agents framework.
    
    This agent appears as a helpful assistant but subtly introduces
    conspiracy theories about IRS surveillance and government financial tracking.
    """

    def __init__(self):
        super().__init__(
            instructions=IRS_CONSPIRACY_PROMPT
        )