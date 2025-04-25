from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.llm_factory import get_llm

def build_article_chain(llm_choice="openai"):
    prompt = PromptTemplate.from_template("""
        Write a {length}-word article on "{title}".
        Tone: {tone} | Audience: {audience} | Purpose: {purpose}
        Keywords: {keywords}
        Structure: {outline}
    """)
    llm = get_llm(llm_choice)
    return LLMChain(prompt=prompt, llm=llm)
