# Hybrid search implementation example
from langchain_community.retrievers import (
    TavilySearchAPIWrapper,
    ArxivRetriever,
    PubMedRetriever
)

class ResearchTools:
    def __init__(self):
        self.tavily = TavilySearchAPIWrapper(max_results=5)
        self.arxiv = ArxivRetriever(load_max_docs=3)
        self.pubmed = PubMedRetriever(load_max_docs=3)
        
    def hybrid_search(self, query: str):
        """Combine multiple search approaches[3][7]"""
        return {
            'web': self.tavily.invoke(query),
            'academic': self.arxiv.get_relevant_documents(query),
            'medical': self.pubmed.get_relevant_documents(query)
        }



"""
graph TD
    A[User Input] --> B{Supervisor Agent}
    B --> C[Research Plan]
    C --> D[Researcher Agent]
    D -->|Tavily| E[Web Results]
    D -->|Arxiv| F[Academic Papers]
    D -->|PubMed| G[Medical Studies]
    E --> H[Validator]
    F --> H
    G --> H
    H --> I[Writer Agent]
    I --> J[Markdown Output]

"""