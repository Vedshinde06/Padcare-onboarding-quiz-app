from .loader import load_document
from .chunker import chunk_documents
from .vectorstore import get_vectorstore


def ingest_document(file_path: str, department: str = "hr"):
    # 1. Load
    documents = load_document(file_path)

    # 2. Chunk
    chunks = chunk_documents(documents)

    # 3. Add metadata
    for chunk in chunks:
        chunk.metadata["department"] = department
        chunk.metadata["source_file"] = file_path

    # 4. Store in vector DB
    vectorstore = get_vectorstore()
    vectorstore.add_documents(chunks)
    vectorstore.persist()

    return len(chunks)