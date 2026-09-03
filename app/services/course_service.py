from fastapi import HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from app.models.models import Course


class CourseService:

    @staticmethod
    def get_all(session):
        return session.scalars(select(Course).options(selectinload(Course.lessons))).all()

    @staticmethod
    def create(payload, session, user_id):
        course = Course(**payload.model_dump(), owner_id=user_id)
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

    @staticmethod
    def find(course_id, session):
        course = session.scalar(select(Course).where(Course.id == course_id).options(selectinload(Course.lessons)))
        if course is None:
            raise ValueError("id не найден")
        return course

    @staticmethod
    def patch(payload, session, user_id):
        if payload.id != Course.id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Курс с таким id не найден')
        course = session.scalar(select(Course).where(Course.id == payload.id))
        if int(user_id) != course.owner_id:
            raise ValueError("Пользователь не является владельцем курса")
        session.execute(
            update(Course).where(Course.id == payload.id).values(
                **payload.model_dump(exclude={'id'}, exclude_unset=True))
        )
        session.commit()

    @staticmethod
    def delete(id, session, user_id):
        course = session.scalar(select(Course).where(Course.id == id))
        if int(user_id) != course.owner_id:
            raise ValueError("Пользователь не является владельцем курса")
        session.delete(course)
        session.commit()


course_service = CourseService()
