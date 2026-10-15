from fastapi import HTTPException, status

from sqlalchemy import select, update
from app.models.models import Lesson, Course
from sqlalchemy.orm import Session

from app.schemas.lesson import LessonFind, LessonCreate, LessonPatch, LessonPatchResponse


class LessonService:

    @staticmethod
    def get_all(session: Session) -> list[Lesson]:
        return session.scalars(select(Lesson)).all()

    @staticmethod
    def create(payload: LessonCreate, session: Session, user_id: int) -> Lesson:
        course = session.scalar(select(Course).where(Course.id == payload.course_id))
        if int(user_id) != course.owner_id:
            raise ValueError("Пользователь не является владельцем курса")
        lesson = Lesson(**payload.model_dump())
        session.add(lesson)
        session.commit()
        session.refresh(lesson)
        return lesson

    @staticmethod
    def find(payload: LessonFind, session: Session) -> Lesson:
        lesson = session.scalar(select(Lesson).where(Lesson.id == payload.id))
        if lesson is None:
            raise ValueError("Урок с указанным id не найден")
        return lesson

    @staticmethod
    def patch(payload: LessonPatch, session: Session, user_id: int) -> LessonPatchResponse:
        lesson = session.scalar(select(Lesson).where(Lesson.id == payload.id))
        if not lesson:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Урок с таким id не найден")
        if int(user_id) != lesson.owner_id:
            raise ValueError("Пользователь не является владельцем урока")
        session.execute(
            update(Lesson).where(Lesson.id == payload.id).values(**payload.model_dump(exclude={'id'}, exclude_unset=True))
        )
        session.commit()
        return LessonPatchResponse(id=lesson.id, name=lesson.name)

    @staticmethod
    def delete(id: int, session: Session, user_id: int) -> None:
        lesson = session.scalar(select(Lesson).where(Lesson.id == id))
        if not lesson:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Урок с таким id не найден")
        if int(user_id) != lesson.owner_id:
            raise ValueError("Пользователь не является владельцем урока")
        session.delete(lesson)
        session.commit()


lesson_service = LessonService()
