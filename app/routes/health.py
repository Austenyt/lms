from fastapi import APIRouter

health_router = APIRouter(tags=["health"])


@health_router.get("/health")
def health() -> dict:
    return {"status": "ok"}
