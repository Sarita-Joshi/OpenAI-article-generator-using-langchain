# tools/knowledge_tool.py
from langchain.agents import Tool
from retriever.query import query_docs

def get_knowledge_tool(persist_id="default_doc"):
    return Tool(
        name="KnowledgeBase",
        func=lambda q: query_docs(q, persist_id=persist_id),
        description="Useful for answering questions based on uploaded documents"
    )
