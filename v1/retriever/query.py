import os
from langchain_community.vectorstores import FAISS
from v1.utils.embeddings_factory import get_embeddings

VECTOR_DIR = "data/vectorstore"



def query_docs(query: str, persist_id: str, k=3) -> str:
    db_path = os.path.join(VECTOR_DIR, persist_id)
    if not os.path.exists(db_path):
        return "No indexed document found. Please upload and ingest first."

    embeddings = get_embeddings(provider="huggingface", model_name="all-MiniLM-L6-v2")
    db = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
    results = db.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in results])
