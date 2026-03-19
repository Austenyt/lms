from fastapi import APIRouter

students_router = APIRouter(tags=["Students"])

@students_router.get("/students/")
def students():
    return {"status": "ok"}

@students_router.get("/students/{id}")
def student(id: int):
    return {"status": "ok"}

@students_router.post("/students/")
def create_student():
    return {"status": "ok"}

@students_router.put("/students/{id}")
def update_student(id: int):
    return {"status": "ok"}

@students_router.delete("/students/{id}")
def delete_student(id: int):
    return {"status": "ok"}
