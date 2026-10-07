from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.services.course_service import course_service
from sqlalchemy.orm import Session

from app.models.models import User


class UserService:

    @staticmethod
    def get_all(session: Session):
        return session.scalars(select(User).options(selectinload(User.courses))).all()

    @staticmethod
    def find(id: int, session: Session):
        user = session.scalar(select(User).where(User.id == id).options(selectinload(User.courses)))
        if user is None:
            raise ValueError("Студент не найден")
        return user

    def delete(self, id: int, session: Session):
        user = self.find(id, session)
        session.delete(user)
        session.commit()

    def enroll(self, course_id: int, user_id: int, session: Session):
        course = course_service.find(course_id, session)
        user = self.find(user_id, session)

        user.courses.append(course)
        session.commit()
        return user

    def dismiss(self, course_id: int, user_id: int, session: Session):
        course = course_service.find(course_id, session)
        user = self.find(user_id, session)

        user.courses.remove(course)
        session.commit()
        return user


user_service = UserService()
