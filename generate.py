from agents.research_agent import run_research_query
from chains.article_chain import build_article_chain


def generate_article(params):
    chain = build_article_chain(params["llm_choice"])
    return chain.run({
        "title": params["title"],
        "keywords": ", ".join(params["keywords"]),
        "length": str(params["length"]),
        "tone": params["tone"],
        "audience": params["audience"],
        "outline": ", ".join(params["outline"]),
        "purpose": params["purpose"]
    })

if __name__=="__main__":
    generate_article()