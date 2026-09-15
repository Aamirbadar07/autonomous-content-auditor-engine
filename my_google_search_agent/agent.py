"""
Travel Scout Agent equipped with the native Google Search tool for real-time grounding.
Leverages Gemini 3.5 Flash for high-speed, fact-checked destination scouting.
"""
from __future__ import annotations

import os
from google.adk.agents import Agent
from google.adk.tools import google_search

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.5-flash")

agent = Agent(
    name="my_google_search_agent",
    model=MODEL_NAME,
    instruction=(
        "You are an elite Travel Scout for Cymbal Travel. "
        "Your mission is to research travel destinations and discover upcoming cultural events, "
        "festivals, local landmarks, seasonal activities, and logistics. "
        "Always use the Google Search tool to verify dates, current schedules, and factual event details. "
        "Cite the real-world sources and provide a concise, engaging summary for prospective travelers."
    ),
    tools=[google_search],
)
