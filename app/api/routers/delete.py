# app/api/routers/delete.py
from fastapi import APIRouter, HTTPException, Request
from app.api import schemas
from app.models.driver import FileDriver
from app.api.utils import FileUtils
from app.core.urls import URLS

router = APIRouter()

class DeleteRouter:
    @staticmethod
    @router.post(URLS.DELETE)
    def delete_file(request: schemas.FileDeleteRequest, req: Request):
        db = req.state.db  # Access the db session
        if not FileDriver.delete_file_record(db, request.file_id):
            raise HTTPException(status_code=404, detail="File not found.")

        if not FileUtils.delete_file(request.file_id):
            raise HTTPException(status_code=500, detail="Failed to delete file from server.")

        return {"message": "File deleted successfully."}
