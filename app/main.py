from fastapi import FastAPI
from app.routes.health import health_router
from app.routes.courses import courses_router

app = FastAPI()
app.include_router(health_router)
app.include_router(courses_router)
