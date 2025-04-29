import pytest
from agents.writer_agent import write_article

def test_article_writing():
    result = write_article(
        topic="Impact of AI on Healthcare",
        outline="Introduction, Emerging Trends, Challenges, Future Outlook, Conclusion",
        research="AI is impacting diagnosis, treatment, and patient monitoring.",
        audience="professionals",
        tone="informative",
        purpose="blog post",
        keywords="AI, Healthcare",
        length=1000,
        llm_choice="gemini"
    )
    assert isinstance(result, str)
    assert len(result) > 100