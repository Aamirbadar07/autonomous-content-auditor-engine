"""
Root SequentialAgent orchestrating the Critic-to-Reviser audit pipeline.
Executes an end-to-end multi-agent verification flow:
  Phase 1: auditor_critic (Identifies claims and cross-examines via Google Search)
  Phase 2: auditor_reviser (Rewrites content incorporating corrections and verified facts)
"""
from __future__ import annotations

from google.adk.agents import SequentialAgent
from .critic.agent import critic_agent
from .reviser.agent import reviser_agent

agent = SequentialAgent(
    name="llm_auditor",
    sub_agents=[critic_agent, reviser_agent],
    description=(
        "Enterprise Autonomous Content Auditor and Fact-Checking Engine. "
        "Orchestrates a grounded critique-to-revision pipeline ensuring published "
        "marketing brochures and technical claims meet strict factual standards."
    ),
)

# ADK's loader resolves agents by the name `root_agent`.
root_agent = agent
