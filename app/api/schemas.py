# app/api/schemas.py
from pydantic import BaseModel
from typing import List

class FileUploadResponse(BaseModel):
    file_id: str
    size: int
    name: str

class FileDeleteRequest(BaseModel):
    file_id: str

class FileDetailsRequest(BaseModel):
    files: List[str]
