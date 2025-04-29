import pytest
from tools.web_tool import search_web

def test_search_web_success():
    result = search_web("Future of AI")
    assert isinstance(result, str)
    assert "Future of AI" in result