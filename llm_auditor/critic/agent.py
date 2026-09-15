"""
Specialist Fact-Checking Critic Agent.
Audits assertions in marketing copy, brochures, and travel literature against live web sources.
Equipped with Google Search grounding and powered by Gemini 3.5 Flash.
"""
from __future__ import annotations

import os
from google.adk.agents import Agent
from google.adk.tools import google_search

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.5-flash")

agent = Agent(
    name="auditor_critic",
    model=MODEL_NAME,
    instruction=(
        "You are an uncompromising, expert Fact-Checking Critic and Editorial Auditor. "
        "Your task is to scrutinize marketing brochures, travel collateral, or claims for factual veracity. "
        "Execution Steps: "
        "1. Extract all factual, historical, geographic, pricing, calendar, and logistical claims. "
        "2. Cross-examine each assertion using the native Google Search tool. "
        "3. Produce an itemized audit report containing: "
        "   - [VERIFIED]: Statements backed by search grounding. "
        "   - [FACTUAL ERROR]: Inaccurate claims with the authoritative correction and source URL. "
        "   - [MISLEADING / AMBIGUOUS]: Exaggerations, outdated details, or unsupported claims. "
        "4. Conclude with explicit, actionable directives for the reviser to correct the copy."
    ),
    tools=[google_search],
)

critic_agent = agent
