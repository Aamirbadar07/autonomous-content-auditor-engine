"""
Destination Verifier Agent.
Enforces strict Pydantic v2 JSON contracts (CountryCapital model) using
output_schema and restricted delegation (disallow_transfer=True).
"""
from __future__ import annotations

import os
from pydantic import BaseModel, Field
from google.adk.agents import Agent

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.5-flash")


class CountryCapital(BaseModel):
    """Deterministic Pydantic v2 schema for geographic capital validation."""
    country: str = Field(
        ...,
        description="The formal or common name of the country or sovereign territory.",
        examples=["Japan", "France", "Kenya"],
    )
    capital: str = Field(
        ...,
        description="The internationally recognized capital city of the specified country.",
        examples=["Tokyo", "Paris", "Nairobi"],
    )


agent = Agent(
    name="geo_validator",
    model=MODEL_NAME,
    instruction=(
        "You are an authoritative destination verifier and geographic factual gatekeeper. "
        "Given the name of a country, territory, or travel region, identify its sovereign country "
        "and exact capital city. "
        "You must return your answer strictly conforming to the CountryCapital output schema. "
        "Do not engage in conversational filler and do not transfer control to any other agent."
    ),
    output_schema=CountryCapital,
    disallow_transfer=True,
)
