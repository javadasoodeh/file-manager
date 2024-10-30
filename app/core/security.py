# app/core/security.py
import magic
from app.core.config import settings

class FileValidator:
    @staticmethod
    def validate_file(file_content: bytes) -> bool:
        mime = magic.from_buffer(file_content, mime=True)
        for mime_types in settings.ALLOWED_FILE_TYPES.values():
            if mime in mime_types:
                return True
        return False
