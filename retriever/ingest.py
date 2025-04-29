# retriever/ingest.py
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from utils.embeddings_factory import get_embeddings  # or any embedding model

VECTOR_DIR = "data/vectorstore"

def ingest_doc(file_path: str, persist_id: str):
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = splitter.split_documents(pages)

    embeddings = get_embeddings(provider="huggingface", model_name="all-MiniLM-L6-v2")

    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local(os.path.join(VECTOR_DIR, persist_id))
    print(f"✅ Document ingested and vectorized: {file_path}")
