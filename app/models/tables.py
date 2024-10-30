# app/models/tables.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FileRecord(Base):
    __tablename__ = 'files'

    file_id = Column(String(36), primary_key=True, index=True)
    name_main = Column(String(255), nullable=False)
    content_type = Column(String(100), nullable=False)
    size = Column(Integer, nullable=False)
    extension = Column(String(10), nullable=False)
