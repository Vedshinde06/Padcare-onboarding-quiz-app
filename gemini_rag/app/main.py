from fastapi import FastAPI
from pydantic import BaseModel
import vertexai
from vertexai.preview.generative_models import GenerativeModel

app = FastAPI()

vertexai.init(project="YOUR_PROJECT_ID", location="us-central1")

model = GenerativeModel("gemini-1.5-pro")

class Query(BaseModel):
    question: str

@app.post("/query")
def query(data: Query):
    response = model.generate_content(
        data.question,
        retrieval={
            "datastore": "YOUR_DATASTORE_FULL_PATH"
        }
    )
    return {"answer": response.text}