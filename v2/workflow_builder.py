from langgraph.graph import StateGraph, START, END
from graph_flow.state import ArticleState
from graph_flow.nodes import *

def build_workflow(llm_adapter):
    graph = StateGraph(ArticleState)

    graph.add_node("web_researcher", web_researcher)
    graph.add_node("academic_researcher", academic_researcher)
    graph.add_node("source_validator", source_validator)
    graph.add_node("outline_generator", outline_generator)
    graph.add_node("section_writer", section_writer)
    graph.add_node("style_editor", style_editor)
    graph.add_node("fact_checker", fact_checker)
    graph.add_node("plagiarism_detector", plagiarism_detector)
    graph.add_node("seo_optimizer", seo_optimizer)
    graph.add_node("output_formatter", output_formatter)

    graph.add_edge(START, "web_researcher")
    graph.add_edge("web_researcher", "academic_researcher")
    graph.add_edge("academic_researcher", "source_validator")
    graph.add_edge("source_validator", "outline_generator")
    graph.add_edge("outline_generator", "section_writer")
    graph.add_edge("section_writer", "style_editor")
    graph.add_edge("style_editor", "fact_checker")
    graph.add_edge("fact_checker", "plagiarism_detector")
    graph.add_edge("plagiarism_detector", "seo_optimizer")
    graph.add_edge("seo_optimizer", "output_formatter")
    graph.add_edge("output_formatter", END)

    return graph.compile()
