from fastapi import APIRouter, Depends
from app.services.course_service import course_service
from app.schemas.course import CourseCreate, CoursePatch, CourseFind
from app.db.database import get_session

courses_router = APIRouter(tags=["courses"])


@courses_router.get("/courses")
def courses(session=Depends(get_session)):
    return course_service.get_all(session)


@courses_router.post("/courses/{course_id}")
def find(payload: CourseFind, session=Depends(get_session)):
    try:
        return course_service.find(payload.id, session)
    except ValueError:
        return {"message": "Курса с таким id не существует"}


@courses_router.post("/courses")
def create(payload: CourseCreate, session=Depends(get_session)):
    course_service.create(payload.name, payload.qty, session)
    return {"message": "Курс успешно добавлен!"}


@courses_router.patch("/courses/{course_id}")
def patch(payload: CoursePatch, session=Depends(get_session)):
    try:
        if payload.name is not None:
            course_service.rename(payload.id, payload.name, session)
        if payload.qty is not None:
            course_service.change_qty(payload.id, payload.qty, session)
        return course_service.find(payload.id, session)
    except ValueError:
        return {"message": "Курса с таким id не существует"}


@courses_router.delete("/courses/{course_id}")
def delete(payload: CourseFind, session=Depends(get_session)):
    try:
        course_service.delete(payload.id, session)
        return {"message": "OK"}
    except ValueError:
        return {"message": "Курса с таким id не существует"}

"""
@courses_router.get("/courses")
def courses():
    return course_service.get_all()


@courses_router.post("/courses/{course_id}")
def find(payload: CourseFind):
    try:
        return course_service.find(payload.id)
    except ValueError:
        return {"message": "Курса с таким id не существует"}


@courses_router.post("/courses")
def create(payload: CourseCreate):
    course_service.create(payload.id, payload.name, payload.qty)
    return {"message": "Курс успешно добавлен!"}


@courses_router.patch("/courses/{course_id}")
def patch(payload: CoursePatch):
    try:
        if payload.name is not None:
            course_service.rename(payload.id, payload.name)
        if payload.qty is not None:
            course_service.change_qty(payload.id, payload.qty)
        return course_service.find(payload.id)
    except ValueError:
        return {"message": "Курса с таким id не существует"}


@courses_router.delete("/courses/{course_id}")
def delete(payload: CourseFind):
    try:
        course_service.delete(payload.id)
        return courses()
    except ValueError:
        return {"message": "Курса с таким id не существует"}
"""