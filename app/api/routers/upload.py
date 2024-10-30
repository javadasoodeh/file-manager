# app/api/routers/upload.py
from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from app.api import schemas
from app.models.driver import FileDriver
from app.core.config import settings
from app.core.security import FileValidator
from app.api.utils import FileUtils
from app.core.urls import URLS
import uuid
import os
import magic

router = APIRouter()


class UploadRouter:
    @staticmethod
    @router.post(URLS.UPLOAD, response_model=schemas.FileUploadResponse)
    async def upload_file(request: Request, file: UploadFile = File(...)):
        file_content = await file.read()
        if len(file_content) > settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024:
            raise HTTPException(status_code=400, detail="File size exceeds the maximum allowed size.")

        if not FileValidator.validate_file(file_content):
            raise HTTPException(status_code=400, detail="File type not allowed.")

        file_id = str(uuid.uuid4())
        file_extension = os.path.splitext(file.filename)[1].lstrip('.')
        content_type = magic.from_buffer(file_content, mime=True)

        FileUtils.save_file(file_content, file_id)

        db = request.state.db  # Access the db session

        FileDriver.create_file_record(
            db=db,
            file_id=file_id,
            name_main=file.filename,
            content_type=content_type,
            size=len(file_content),
            extension=file_extension
        )

        return schemas.FileUploadResponse(
            file_id=file_id,
            size=len(file_content),
            name=file.filename
        )
