"""
Structural tests for the agent definitions. No model calls and no credentials:
these assert the contracts ADK relies on to load and wire the agents, which is
exactly where this repository previously failed.
"""
from __future__ import annotations

import importlib

import pytest
from google.adk.agents import BaseAgent, LlmAgent, SequentialAgent

# The packages ADK will discover as runnable agent directories.
TOP_LEVEL_AGENTS = ["my_google_search_agent", "geo_validator", "llm_auditor"]


@pytest.mark.parametrize("package", TOP_LEVEL_AGENTS)
def test_package_exposes_root_agent(package):
    """ADK's loader resolves `<package>.agent.root_agent` or `<package>.root_agent`."""
    module = importlib.import_module(package)
    assert hasattr(module, "root_agent"), f"{package} exposes no root_agent"
    assert isinstance(module.root_agent, BaseAgent)


@pytest.mark.parametrize("package", TOP_LEVEL_AGENTS)
def test_agent_module_exposes_root_agent(package):
    module = importlib.import_module(f"{package}.agent")
    assert isinstance(module.root_agent, BaseAgent)


def test_geo_validator_imports_and_is_isolated():
    """The invalid `disallow_transfer` kwarg used to raise at import time."""
    from geo_validator import CountryCapital
    from geo_validator.agent import root_agent

    assert root_agent.output_schema is CountryCapital
    # ADK does not infer these from output_schema, so they must be explicit.
    assert root_agent.disallow_transfer_to_parent is True
    assert root_agent.disallow_transfer_to_peers is True


def test_country_capital_schema():
    from geo_validator import CountryCapital

    assert CountryCapital(country="Canada", capital="Ottawa").capital == "Ottawa"
    with pytest.raises(Exception):
        CountryCapital(country="Canada")


def test_auditor_is_a_two_stage_pipeline_in_order():
    from llm_auditor.agent import root_agent

    assert isinstance(root_agent, SequentialAgent)
    assert [sub.name for sub in root_agent.sub_agents] == ["auditor_critic", "auditor_reviser"]


def test_critic_publishes_its_report_to_state():
    from llm_auditor.critic.agent import root_agent

    assert isinstance(root_agent, LlmAgent)
    assert root_agent.output_key == "criticism"
    assert root_agent.tools, "critic must carry the google_search tool"


def test_reviser_binds_to_the_critic_report():
    """The handoff is a declared contract, not an accident of turn ordering."""
    from llm_auditor.critic.agent import root_agent as critic
    from llm_auditor.reviser.agent import root_agent as reviser

    assert "{" + critic.output_key + "}" in reviser.instruction


def test_search_agent_has_search_tool():
    from my_google_search_agent.agent import root_agent

    assert root_agent.tools
