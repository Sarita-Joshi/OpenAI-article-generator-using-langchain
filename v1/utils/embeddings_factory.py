# utils/embedding_factory.py

import os
from langchain_community.embeddings import HuggingFaceEmbeddings

try:
    from langchain_community.embeddings import OpenAIEmbeddings
except ImportError:
    OpenAIEmbeddings = None

try:
    from InstructorEmbedding import INSTRUCTOR
except ImportError:
    INSTRUCTOR = None


def get_embeddings(provider="huggingface", model_name="all-MiniLM-L6-v2"):
    """
    Returns an embedding model based on the specified provider.

    Args:
        provider (str): Options - "huggingface", "instructor", "openai"
        model_name (str): HuggingFace model or OpenAI model

    Returns:
        A langchain-compatible Embedding class
    """

    if provider == "huggingface":
        return HuggingFaceEmbeddings(model_name=model_name)

    elif provider == "instructor":
        if INSTRUCTOR is None:
            raise ImportError("InstructorEmbedding not installed. Install with: pip install InstructorEmbedding")
        instructor_model = INSTRUCTOR(model_name)
        return HuggingFaceEmbeddings(model=instructor_model)

    elif provider == "openai":
        if OpenAIEmbeddings is None:
            raise ImportError("OpenAIEmbeddings not installed. Install openai package.")
        return OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

    else:
        raise ValueError(f"Unknown embedding provider: {provider}")
