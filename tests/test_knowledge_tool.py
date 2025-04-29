import pytest
import os
from retriever.ingest import ingest_doc
from tools.knowledge_tool import get_knowledge_tool

DUMMY_PDF_PATH = "data/uploads/research.pdf"
PERSIST_ID = "test_doc"

@pytest.mark.order(1)
def test_ingest_dummy_document():
    # Ensure dummy PDF exists
    assert os.path.exists(DUMMY_PDF_PATH), f"Dummy PDF not found at {DUMMY_PDF_PATH}"
    
    # Ingest document
    ingest_doc(file_path=DUMMY_PDF_PATH, persist_id=PERSIST_ID)

    # Check if vectorstore was created
    vectorstore_path = os.path.join("data/vectorstore", PERSIST_ID)
    assert os.path.exists(vectorstore_path), "Vectorstore was not created after ingestion."

@pytest.mark.order(2)
def test_query_knowledge_tool():
    kb_tool = get_knowledge_tool(persist_id=PERSIST_ID)
    result = kb_tool.run("What is the main topic of the paper?")
    assert isinstance(result, str)
    assert len(result) > 10  # Should return something meaningful
