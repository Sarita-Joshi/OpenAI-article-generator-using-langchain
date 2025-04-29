from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.llm_factory import get_llm

def generate_outline(topic, audience, tone, purpose, llm_choice="openai"):
    template=("""
    Create a high-quality, structured article outline for the topic: "{topic}".
    - Audience: {audience}
    - Tone: {tone}
    - Purpose: {purpose}
    Provide 5 to 7 section titles as a list.
    """)

    prompt = PromptTemplate(
        input_variables=['topic', 'audience', 'tone', 'purpose'],
        template=template
    )

    llm = get_llm(model_choice=llm_choice, temperature=0.6)
    chain = prompt | llm
    results =  chain.invoke(input={
        "topic": topic,
        "audience": audience,
        "tone": tone,
        "purpose": purpose,
    })

    return results.content
    
