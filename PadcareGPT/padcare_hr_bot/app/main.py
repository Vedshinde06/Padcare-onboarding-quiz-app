from fastapi import FastAPI
from app.config import chat_model, embedding_model
from app.api.admin_routes import router as admin_router


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/test-llm")
def test_llm():
    response = chat_model.generate_content("Say hello like an HR assistant.")
    return {"response": response.text}

@app.get("/test-embed")
def test_embed():
    embeddings = embedding_model.get_embeddings(["This is a test"])
    return {"vector_length": len(embeddings[0].values)}

app.include_router(admin_router)

@app.get("/health")
def health():
    return {"status": "ok"}