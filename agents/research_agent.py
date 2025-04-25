from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from tools.tool_wrappers import get_basic_tools

def build_research_agent():
    tools = get_basic_tools()
    llm = ChatOpenAI(temperature=0.5)
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent

def run_research_query(topic: str) -> str:
    agent = build_research_agent()
    return agent.run(f"Research the topic '{topic}' and provide a brief overview with 3 key facts.")
