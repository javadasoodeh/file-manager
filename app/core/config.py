# app/core/config.py
from pydantic import BaseSettings
from typing import Dict, List

class Settings(BaseSettings):
    APP_NAME: str = "File Manager Service"
    DATABASE_URL: str
    MAX_UPLOAD_SIZE_MB: int = 100
    ALLOWED_FILE_TYPES: Dict[str, List[str]] = {
        "documents": [
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ],
        "images": ["image/jpeg", "image/png", "image/gif"],
        "audio": ["audio/mpeg", "audio/x-wav"],
        "video": ["video/mp4", "video/x-msvideo"],
        "archives": ["application/zip", "application/x-tar"],
    }
    STORAGE_PATH: str = "./storage/"

    class Config:
        env_file = ".env"

settings = Settings()
