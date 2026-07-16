from fastapi import FastAPI

from app.routes.auth import auth_router
from app.routes.health import health_router
from app.routes.courses import courses_router
from app.routes.frontend import frontend_router
from fastapi.staticfiles import StaticFiles
from app.config import config
from app.routes.lessons import lessons_router
from app.routes.students import students_router
from app.routes.auth import auth_router

app = FastAPI()
app.include_router(health_router)
app.include_router(courses_router)
app.include_router(frontend_router)
app.include_router(lessons_router)
app.include_router(students_router)
app.include_router(auth_router)

app.mount("/static", StaticFiles(directory=config.frontend_dir), name="static")
