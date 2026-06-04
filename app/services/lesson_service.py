from sqlalchemy import select, update
from app.models.course import Lesson

class LessonService:

    def get_all(self, session):
        return session.scalars(select(Lesson)).all()


    def create(self, name, content, session):
        lesson = Lesson(
            name=name,
            content=content,
        )
        session.add(lesson)
        session.commit()
        session.refresh(lesson)
        return lesson


    def find(self, id, session):
        lesson = session.get(Lesson, id)
        if lesson is None:
            raise ValueError("Урок с указанным id не найден")
        return lesson


    def patch(self, payload, session):
        session.execute(
            update(Lesson).where(Lesson.id == payload.id).values(**payload.model_dump(exclude={'id'}, exclude_unset=True))
        )
        session.commit()


    def delete(self, id, session):
        lesson = self.find(id, session)
        session.delete(lesson)
        session.commit()


lesson_service = LessonService()
