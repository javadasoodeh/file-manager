# app/api/routers/details.py
from fastapi import APIRouter, HTTPException, Request
from app.api import schemas
from app.models.driver import FileDriver
from app.core.urls import URLS

router = APIRouter()

class DetailsRouter:
    @staticmethod
    @router.post(URLS.DETAILS)
    def get_file_details(request: schemas.FileDetailsRequest, req: Request):
        db = req.state.db  # Access the db session
        files = FileDriver.get_files_details(db, request.files)
        if not files:
            raise HTTPException(status_code=404, detail="Files not found.")

        return [
            {
                "file_id": file.file_id,
                "name": file.name_main,
                "size": file.size,
                "extension": file.extension,
                "content_type": file.content_type
            } for file in files
        ]
