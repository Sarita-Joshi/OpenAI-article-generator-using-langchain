from graph.workflow_builder import build_workflow
from graph.state import ArticleState
from graph.llm_adapter import LLMAdapter

def generate_article_v2_graph(prompt: str, llm_config: dict):
    llm = LLMAdapter(llm_config['provider'], **llm_config['params'])
    workflow = build_workflow(llm)

    initial_state = ArticleState(
        input_query=prompt,
        research_data=[],
        outline="",
        draft=[],
        revisions=[],
        quality_score=0.0
    )

    return workflow.invoke(initial_state)
