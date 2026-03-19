from fastapi import FastAPI
from app.routes.health import health_router


app = FastAPI()
app.include_router(health_router)