from sqlalchemy import select, update
from sqlalchemy.orm import selectinload

from app.models.models import Course


class CourseService:

    @staticmethod
    def get_all(session):
        return session.scalars(select(Course).options(selectinload(Course.lessons))).all()

    @staticmethod
    def create(payload, session):
        course = Course(**payload.model_dump())
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
    def patch(payload, session):
        session.execute(
            update(Course).where(Course.id == payload.id).values(
                **payload.model_dump(exclude={'id'}, exclude_unset=True))
        )
        session.commit()

    def delete(self, id, session):
        course = self.find(id, session)
        session.delete(course)
        session.commit()


course_service = CourseService()
