# app/main.py
from fastapi import FastAPI, Request
from app.api.routers.upload import router as upload_router
from app.api.routers.download import router as download_router
from app.api.routers.delete import router as delete_router
from app.api.routers.details import router as details_router
from app.core.config import settings
from app.models.meta import Database

app = FastAPI(title=settings.APP_NAME)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = None
    try:
        request.state.db = Database.SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Include the routers
app.include_router(upload_router)
app.include_router(download_router)
app.include_router(delete_router)
app.include_router(details_router)
