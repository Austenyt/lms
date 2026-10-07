from sqlalchemy import select, update
from app.models.models import Lesson, Course
from sqlalchemy.orm import Session

from app.schemas.lesson import LessonFind, LessonCreate, LessonPatch


class LessonService:

    @staticmethod
    def get_all(session: Session):
        return session.scalars(select(Lesson)).all()

    @staticmethod
    def create(payload: LessonCreate, session: Session, user_id: int):
        course = session.scalar(select(Course).where(Course.id == payload.course_id))
        if user_id != course.owner_id:
            raise ValueError("Пользователь не является владельцем курса")
        lesson = Lesson(**payload.model_dump())
        session.add(lesson)
        session.commit()
        session.refresh(lesson)
        return lesson

    @staticmethod
    def find(payload: LessonFind, session: Session):
        lesson = session.scalar(select(Lesson).where(Lesson.id == payload.id))
        if lesson is None:
            raise ValueError("Урок с указанным id не найден")
        return lesson

    @staticmethod
    def patch(payload: LessonPatch, session: Session):
        if payload.name and payload.content is None:
            raise ValueError("Пустой запрос")
        session.execute(
            update(Lesson).where(Lesson.id == payload.id).values(**payload.model_dump(exclude={'id'}, exclude_unset=True))
        )
        session.commit()

    @staticmethod
    def delete(id: int, session: Session):
        lesson = session.scalar(select(Lesson).where(Lesson.id == id))
        session.delete(lesson)
        session.commit()


lesson_service = LessonService()
