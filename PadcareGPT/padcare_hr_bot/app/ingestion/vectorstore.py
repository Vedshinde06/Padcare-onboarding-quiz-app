from langchain_google_vertexai import VertexAIEmbeddings
from langchain_community.vectorstores import Chroma
import vertexai
import os

PROJECT_ID = "ai-padcaregpt-dev"
LOCATION = "us-central1"


def initialize_vertex():
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION
    )


def get_embeddings():
    initialize_vertex()

    return VertexAIEmbeddings(
        model_name="text-embedding-004"
    )


def get_vectorstore(persist_directory="chroma_db"):
    embeddings = get_embeddings()

    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )