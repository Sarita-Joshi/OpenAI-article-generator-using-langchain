import pytest
from agents.research_agent import run_research_query

def test_research_agent_query():
    result = run_research_query("Future of AI", llm_choice="groq")
    assert isinstance(result, str)
    assert len(result) > 30