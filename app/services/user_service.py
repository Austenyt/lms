from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from app.services.course_service import course_service

from app.models.models import User


class UserService:

    @staticmethod
    def get_all(session):
        return session.scalars(select(User).options(selectinload(User.courses))).all()

    @staticmethod
    def create(payload, session):
        user = User(**payload.model_dump())
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def find(id, session):
        user = session.scalar(select(User).where(User.id == id).options(selectinload(User.courses)))
        if user is None:
            raise ValueError("Студент не найден")
        return user

    @staticmethod
    def patch(payload, session):
        if payload.first_name and payload.last_name is None:
            raise ValueError("Пустой запрос")
        session.execute(update(User).where(User.id == payload.id).values(
            **payload.model_dump(exclude={'id'}, exclude_unset=True)))
        session.commit()

    def delete(self, id, session):
        user = self.find(id, session)
        session.delete(user)
        session.commit()

    def enroll(self, course_id, user_id, session):
        course = course_service.find(course_id, session)
        user = self.find(user_id, session)

        user.courses.append(course)
        session.commit()
        return user

    def dismiss(self, course_id, user_id, session):
        course = course_service.find(course_id, session)
        user = self.find(user_id, session)

        user.courses.remove(course)
        session.commit()
        return user


user_service = UserService()
