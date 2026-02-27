from fastapi import APIRouter, UploadFile, File
import os

from app.ingestion.pipeline import ingest_document 

router = APIRouter()

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/admin/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    chunks_indexed = ingest_document(file_path, department="hr")

    return {
        "message": "File processed successfully",
        "chunks_indexed": chunks_indexed
    }