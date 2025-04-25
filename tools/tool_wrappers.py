from langchain.agents import Tool
from tools.wiki_tool import search_wikipedia

def get_basic_tools():
    return [
        Tool(
            name="Wikipedia",
            func=search_wikipedia,
            description="Useful for getting factual information about a topic from Wikipedia"
        )
    ]
