# app/models/driver.py
from sqlalchemy.orm import Session
from app.models.tables import FileRecord

class FileDriver:
    @staticmethod
    def create_file_record(db: Session, file_id: str, name_main: str, content_type: str, size: int, extension: str):
        file_record = FileRecord(
            file_id=file_id,
            name_main=name_main,
            content_type=content_type,
            size=size,
            extension=extension
        )
        db.add(file_record)
        db.commit()
        db.refresh(file_record)
        return file_record

    @staticmethod
    def get_file_record(db: Session, file_id: str):
        return db.query(FileRecord).filter(FileRecord.file_id == file_id).first()

    @staticmethod
    def delete_file_record(db: Session, file_id: str):
        file_record = FileDriver.get_file_record(db, file_id)
        if file_record:
            db.delete(file_record)
            db.commit()
            return True
        return False

    @staticmethod
    def get_files_details(db: Session, file_ids: list):
        return db.query(FileRecord).filter(FileRecord.file_id.in_(file_ids)).all()
