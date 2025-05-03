from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from v1.utils.llm_factory import get_llm

def summarize_article(article, topic, llm_choice="openai"):
    template = """
    Summarize the following article about "{topic}" in 3-5 bullet points.
    Be concise and cover key insights.
    
    Article:
    {article}
    """

    prompt = PromptTemplate(
        input_variables=['topic', 'article'],
        template=template
    )

    llm = get_llm(model_choice=llm_choice, temperature=0.5)
    chain = prompt | llm
    results =  chain.invoke(input={
       "topic": topic,
        "article": article
    })

    return results.content
