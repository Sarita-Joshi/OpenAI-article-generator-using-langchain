import pytest
from v1.agents.summary_agent import summarize_article

def test_article_summary():
    dummy_article = """
    Artificial Intelligence is rapidly transforming healthcare, enhancing diagnosis, and enabling personalized treatments.
    """
    result = summarize_article(dummy_article, topic="AI in Healthcare", llm_choice="gemini")
    assert isinstance(result, str)
    assert len(result) > 30