from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredPowerPointLoader,
    Docx2txtLoader,
    UnstructuredExcelLoader
)

def load_document(file_path: str):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)

    elif file_path.endswith(".pptx"):
        loader = UnstructuredPowerPointLoader(file_path)

    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)

    elif file_path.endswith(".xlsx"):
        loader = UnstructuredExcelLoader(file_path)

    else:
        raise ValueError("Unsupported file format")

    return loader.load()