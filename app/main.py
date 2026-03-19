from fastapi import FastAPI
from app.routes.health import health_router
from app.routes.lessons import lessons_router
from app.routes.students import students_router

app = FastAPI()
app.include_router(health_router)
app.include_router(lessons_router)
app.include_router(students_router)
