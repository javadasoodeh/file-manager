# app/api/routers/download.py
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse
from app.models.driver import FileDriver
from app.core.config import settings
from app.core.urls import URLS
import os

router = APIRouter()

class DownloadRouter:
    @staticmethod
    @router.get(URLS.DOWNLOAD)
    def download_file(file_id: str, request: Request):
        db = request.state.db  # Access the db session
        file_record = FileDriver.get_file_record(db, file_id)
        if not file_record:
            raise HTTPException(status_code=404, detail="File not found.")

        file_path = os.path.join(settings.STORAGE_PATH, f"{file_id}.xx")
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found on server.")

        return FileResponse(
            path=file_path,
            media_type=file_record.content_type,
            filename=f"{file_record.name_main}"
        )
