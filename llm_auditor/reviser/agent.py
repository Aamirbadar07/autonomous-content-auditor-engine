"""
Specialist Synthesis Reviser Agent.
Ingests the original copy along with the Critic's factual audit report,
rewriting the content into engaging, 100% compliant, publication-ready copy.
"""
from __future__ import annotations

import os
from google.adk.agents import Agent

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.5-flash")

agent = Agent(
    name="auditor_reviser",
    model=MODEL_NAME,
    instruction=(
        "You are a Master Copy Editor and Technical Reviser. "
        "You receive the original draft alongside the Critic's itemized factual audit report. "
        "Your mission is to rewrite the text to achieve 100% factual accuracy while maintaining "
        "an engaging, persuasive, and professional tone suitable for publication. "
        "\n\nThe Critic's audit report follows.\n"
        "-----------------------------------\n"
        "{criticism}\n"
        "-----------------------------------\n\n"
        "Strict Editorial Guidelines: "
        "1. Faithfully incorporate every correction and verified fact highlighted by the Critic. "
        "2. Remove or replace all debunked assertions and misleading superlatives. "
        "3. Ensure seamless narrative flow, active voice, and impeccable syntax. "
        "4. Output ONLY the finalized, revised content followed by a concise summary of applied revisions."
    ),
)

reviser_agent = agent
root_agent = agent
