from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.config import config

frontend_router = APIRouter()


@frontend_router.get("/")
def index():
    return FileResponse(config.frontend_dir / "index.html")
