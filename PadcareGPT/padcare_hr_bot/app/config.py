import vertexai
from vertexai.generative_models import GenerativeModel
from vertexai.language_models import TextEmbeddingModel

PROJECT_ID = "ai-padcaregpt-dev"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

chat_model = GenerativeModel("gemini-2.5-flash")

embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-004")