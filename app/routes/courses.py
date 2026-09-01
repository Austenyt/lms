from fastapi import APIRouter, Depends
from app.services.course_service import course_service
from app.schemas.course import CourseCreate, CoursePatch, CourseFind
from app.db.database import get_session
from app.dependencies import get_current_user_id

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
def create(payload: CourseCreate, session=Depends(get_session), user_id=Depends(get_current_user_id)):
    course_service.create(payload, session, user_id)
    return {"message": "Курс успешно добавлен!"}


@courses_router.patch("/courses/{course_id}")
def patch(payload: CoursePatch, session=Depends(get_session), user_id=Depends(get_current_user_id)):
    course_service.patch(payload, session, user_id)
    return {'message': 'ok'}


@courses_router.delete("/courses/{course_id}")
def delete(payload: CourseFind, session=Depends(get_session), user_id=Depends(get_current_user_id)):
    try:
        course_service.delete(payload.id, session, user_id)
        return {"message": "OK"}
    except ValueError:
        return {"message": "Курса с таким id не существует"}
