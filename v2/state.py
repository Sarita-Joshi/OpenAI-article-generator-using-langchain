from typing import TypedDict, List, Dict

class ArticleState(TypedDict):
    input_query: str
    research_data: List[Dict]
    outline: str
    draft: List[str]
    revisions: List[str]
    quality_score: float
