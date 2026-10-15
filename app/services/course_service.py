from fastapi import HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import Session

from app.models.models import Course
from app.schemas.course import CourseCreate, CourseFind, CoursePatch, CoursePatchResponse


class CourseService:

    @staticmethod
    def get_all(session: Session) -> list[Course]:
        return session.scalars(select(Course).options(selectinload(Course.lessons))).all()

    @staticmethod
    def create(payload: CourseCreate, session: Session, user_id: int) -> Course:
        course = Course(**payload.model_dump(), owner_id=user_id)
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

    @staticmethod
    def find(payload: CourseFind, session: Session) -> Course:
        course = session.scalar(select(Course).where(Course.id == payload.id).options(selectinload(Course.lessons)))
        if course is None:
            raise ValueError("id не найден")
        return course

    @staticmethod
    def patch(payload: CoursePatch, session: Session, user_id: int) -> CoursePatchResponse:
        course = session.scalar(select(Course).where(Course.id == payload.id))
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Курс с таким id не найден")
        if int(user_id) != course.owner_id:
            raise ValueError("Пользователь не является владельцем курса")
        session.execute(
            update(Course).where(Course.id == payload.id).values(
                **payload.model_dump(exclude={'id'}, exclude_unset=True))
        )
        session.commit()
        return CoursePatchResponse(id=course.id, name=course.name)

    @staticmethod
    def delete(id: int, session: Session, user_id: int) -> None:
        course = session.scalar(select(Course).where(Course.id == id))
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Курс с таким id не найден")
        if int(user_id) != course.owner_id:
            raise ValueError("Пользователь не является владельцем курса")
        session.delete(course)
        session.commit()


course_service = CourseService()
