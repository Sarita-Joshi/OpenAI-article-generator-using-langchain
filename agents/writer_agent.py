from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.llm_factory import get_llm


def write_article(
    topic,
    outline,
    research,
    audience,
    tone,
    purpose,
    keywords,
    length,
    llm_choice="openai",
):
    template = """
    Using the following research: {research}
    Write a {length}-word article titled "{topic}".

    - Audience: {audience}
    - Tone: {tone}
    - Purpose: {purpose}
    - Keywords: {keywords}
    - Structure the content using this outline: {outline}
    Ensure the article is coherent, informative, and engaging.
    """
    prompt = PromptTemplate(
        input_variables=[
            "research",
            "length",
            "topic",
            "audience",
            "tone",
            "purpose",
            "keywords",
            "outline",
        ],
        template=template,
    )

    llm = get_llm(model_choice=llm_choice, temperature=0.5)
    chain = prompt | llm
    results = chain.invoke(
        input={
            "topic": topic,
            "research": research,
            "length": length,
            "audience": audience,
            "tone": tone,
            "purpose": purpose,
            "keywords": keywords,
            "outline": outline,
        }
    )

    return results.content
