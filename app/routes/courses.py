from fastapi import APIRouter
from app.services.course_service import course_service
from app.schemas.course import CourseCreate

courses_router = APIRouter(tags=["courses"])


@courses_router.get("/courses")
def courses():
    return course_service.get_all()


@courses_router.get("/courses/{course_id}")
def find(id: int):
    try:
        return course_service.find(id)
    except ValueError:
        return {"message": "Курса с таким id не существует"}


@courses_router.post("/courses")
def create(payload: CourseCreate):
    course_service.create(payload.id, payload.name, payload.qty)
    return {"message": "Курс успешно добавлен!"}


@courses_router.patch("/courses/{course_id}")
def patch(id: int, name: str = None, qty: int = None):
    try:
        if name is not None:
            course_service.rename(id, name)
        if qty is not None:
            course_service.change_qty(id, qty)
        return course_service.find(id)
    except ValueError:
        return {"message": "Курса с таким id не существует"}


@courses_router.delete("/courses/{course_id}")
def delete(id: int):
    try:
        course_service.delete(id)
        return courses()
    except ValueError:
        return {"message": "Курса с таким id не существует"}
