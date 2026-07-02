from sqlalchemy import select, update
from app.models.models import Lesson


class LessonService:

    @staticmethod
    def get_all(session):
        return session.scalars(select(Lesson)).all()

    @staticmethod
    def create(payload, session):
        lesson = Lesson(**payload.model_dump())
        session.add(lesson)
        session.commit()
        session.refresh(lesson)
        return lesson

    @staticmethod
    def find(id, session):
        lesson = session.get(Lesson, id)
        if lesson is None:
            raise ValueError("Урок с указанным id не найден")
        return lesson

    @staticmethod
    def patch(payload, session):
        session.execute(
            update(Lesson).where(Lesson.id == payload.id).values(**payload.model_dump(exclude={'id'}, exclude_unset=True))
        )
        session.commit()

    def delete(self, id, session):
        lesson = self.find(id, session)
        session.delete(lesson)
        session.commit()


lesson_service = LessonService()
