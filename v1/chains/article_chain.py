# agents/research_agent.py

from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from v1.tools.tool_wrappers import get_basic_tools
from v1.utils.llm_factory import get_llm  # Unified LLM selection

def build_research_agent(llm_choice="openai", temperature=0.5, doc_id="default_doc"):
    tools = get_basic_tools()
    llm = get_llm(model_choice=llm_choice, temperature=temperature)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent

def run_research_query(topic: str, llm_choice="openai") -> str:
    agent = build_research_agent(llm_choice=llm_choice)
    return agent.run(
        f"Research the topic '{topic}' and provide a brief overview with three factual insights."
    )
