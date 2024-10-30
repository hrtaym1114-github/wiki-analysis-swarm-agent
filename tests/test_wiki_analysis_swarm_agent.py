import pytest
from wiki_analysis_swarm_agent import create_research_agent, create_report_agent

def test_create_research_agent():
    agent = create_research_agent()
    assert agent.name == "WikiResearcher"
    assert "調査エージェント" in agent.instructions

def test_create_report_agent():
    agent = create_report_agent()
    assert agent.name == "ReportWriter"
    assert "レポート作成エージェント" in agent.instructions 