# app/api/utils.py
import os
from app.core.config import settings

class FileUtils:
    @staticmethod
    def save_file(file_content: bytes, file_id: str) -> str:
        storage_path = settings.STORAGE_PATH
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
        file_location = os.path.join(storage_path, f"{file_id}.xx")
        with open(file_location, "wb") as buffer:
            buffer.write(file_content)
        return file_location

    @staticmethod
    def delete_file(file_id: str) -> bool:
        file_path = os.path.join(settings.STORAGE_PATH, f"{file_id}.xx")
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
