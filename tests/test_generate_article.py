import pytest
from generate import generate_article

@pytest.mark.parametrize("topic", ["Impact of AI on Healthcare", "Future of AI in Education"])
def test_full_article_generation(topic):
    params = {
        "title": topic,
        "keywords": ["AI", "future", "innovation"],
        "length": 500,
        "tone": "informative",
        "audience": "students",
        "outline": ["Introduction", "Emerging Trends", "Applications", "Challenges", "Conclusion"],
        "purpose": "blog post",
        "language": "en",
        "llm_choice": "groq",
        "auto_research": True,
        "auto_outline": True,
        "include_summary": True,
        "temperature": 0.5,
        "top_p": 1.0
    }
    article = generate_article(params)
    assert isinstance(article, str)
    assert "AI" in article or len(article) > 200