# agents/research_agent.py

from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from tools.tool_wrappers import get_basic_tools
from utils.llm_factory import get_llm  # Unified LLM selection

def build_research_agent(llm_choice="openai", temperature=0.5):
    tools = get_basic_tools()
    llm = get_llm(model_choice=llm_choice, temperature=temperature)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=5,     # <= HARD LIMIT
        early_stopping_method="generate"  # <= STOP and generate output early
    )
    return agent

def run_research_query(topic: str, llm_choice="openai") -> str:
    agent = build_research_agent(llm_choice=llm_choice)
    return agent.invoke(
       input = f"""Research the topic "{topic}" and create a structured brief overview.

- Use trusted sources like Wikipedia, WebSearch, News, and uploaded documents.
- If a source is unavailable, move on without retrying indefinitely.
- Provide 3 to 5 key insights in a clear, concise style.
- Do not hallucinate facts. Base information only on gathered knowledge.
- Summarize in your own words after collecting information.

Your response should be factual, easy to understand, and logically organized.""",
       
    )

#TODO - upgrade to langgraph