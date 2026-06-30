from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from app.services.course_service import course_service

from app.models.course import Student


class StudentsService:

    def get_all(self, session):
        return session.scalars(select(Student)).all()

    def create(self, payload, session):
        student = Student(**payload.model_dump())
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

    def find(self, id, session):
        student = session.scalar(select(Student).where(Student.id == id).options(selectinload(Student.courses)))
        if student is None:
            raise ValueError("Студент не найден")
        return student

    def patch(self, payload, session):
        session.execute(update(Student).where(Student.id == payload.id).values(**payload.model_dump(exclude={'id'}, exclude_unset=True)))
        session.commit()

    def delete(self, id, session):
        student = self.find(id, session)
        session.delete(student)
        session.commit()

    def enroll(self, course_id, student_id, session):
        course = course_service.find(course_id, session)
        student = self.find(student_id, session)

        student.courses.append(course)
        session.commit()
        return student

    def dismiss(self, course_id, student_id, session):
        course = course_service.find(course_id, session)
        student = self.find(student_id, session)

        student.courses.remove(course)
        session.commit()
        return student

student_service = StudentsService()
