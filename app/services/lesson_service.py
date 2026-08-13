from sqlalchemy import select, update
from app.models.models import Lesson, Course


class LessonService:

    @staticmethod
    def get_all(session):
        return session.scalars(select(Lesson)).all()

    @staticmethod
    def create(payload, session, student_id):
        course = session.scalar(select(Course).where(Course.id == payload.course_id))
        if student_id != course.owner_id:
            raise ValueError("Пользователь не является владельцем курса")
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
        if payload.name and payload.content is None:
            raise ValueError("Пустой запрос")
        session.execute(
            update(Lesson).where(Lesson.id == payload.id).values(**payload.model_dump(exclude={'id'}, exclude_unset=True))
        )
        session.commit()

    def delete(self, id, session):
        lesson = self.find(id, session)
        session.delete(lesson)
        session.commit()


lesson_service = LessonService()
