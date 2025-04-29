from agents.research_agent import run_research_query
from agents.outline_agent import generate_outline
from agents.writer_agent import write_article
from agents.summary_agent import summarize_article


def generate_article(params):
    topic = params["title"]
    keywords = ", ".join(params["keywords"])
    length = params["length"]
    tone = params["tone"]
    audience = params["audience"]
    outline_input = ", ".join(params["outline"])
    purpose = params["purpose"]
    llm_choice = params["llm_choice"]

    # Conditional flow based on UI checkboxes
    if params.get("auto_research", True):
        research = run_research_query(topic, llm_choice=llm_choice)
    else:
        research = ""

    if params.get("auto_outline", True):
        outline = generate_outline(topic, audience, tone, purpose, llm_choice=llm_choice)
    else:
        outline = outline_input

    article = write_article(
        topic=topic,
        outline=outline,
        research=research,
        audience=audience,
        tone=tone,
        purpose=purpose,
        keywords=keywords,
        length=length,
        llm_choice=llm_choice
    )

    if params.get("include_summary", True):
        summary = summarize_article(article, topic, llm_choice=llm_choice)
        article += "\n\n---\n\n**Summary:**\n" + summary

    return article
