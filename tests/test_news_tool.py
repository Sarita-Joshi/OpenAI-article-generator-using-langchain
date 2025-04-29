import pytest
from tools.news_tool import get_latest_news

def test_get_latest_news_success():
    result = get_latest_news("Artificial Intelligence")
    assert isinstance(result, str)
    assert "Artificial Intelligence" in result