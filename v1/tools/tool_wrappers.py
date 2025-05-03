from langchain.agents import Tool
from v1.tools.wiki_tool import search_wikipedia
from v1.tools.web_tool import search_web
from v1.tools.news_tool import get_latest_news
from v1.tools.knowledge_tool import get_knowledge_tool

def get_basic_tools(persist_id: str = "default_doc"):
    return [
        Tool(
            name="Wikipedia",
            func=search_wikipedia,
            description="Useful for getting factual information about a topic from Wikipedia"
        ),
        Tool(
            name="WebSearch",
            func=search_web,
            description="Useful for finding latest information using DuckDuckGo search"
        ),
        Tool(
            name="News",
            func=get_latest_news,
            description="Useful for summarizing latest news articles"
        ),
        get_knowledge_tool(persist_id)
    ]