from fastapi import APIRouter

lessons_router = APIRouter(tags=["Lessons"])

@lessons_router.get("/lessons")
def lessons():
    return {"status": "ok"}
