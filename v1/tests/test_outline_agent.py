import pytest
from v1.agents.outline_agent import generate_outline

def test_outline_generation():
    result = generate_outline(
        topic="Impact of AI on Healthcare",
        audience="professionals",
        tone="informative",
        purpose="blog post",
        llm_choice="gemini"
    )
    assert isinstance(result, str)
    assert "Introduction" in result or len(result.splitlines()) >= 5