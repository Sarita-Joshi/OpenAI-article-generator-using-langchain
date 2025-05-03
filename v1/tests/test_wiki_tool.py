import pytest
from v1.tools.wiki_tool import search_wikipedia

def test_search_wikipedia_success():
    result = search_wikipedia("Artificial Intelligence")
    assert isinstance(result, str)
    assert len(result) > 20