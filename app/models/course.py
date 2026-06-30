from app.db.base import Base
from sqlalchemy.orm import Mapped, relationship, Session
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy import Integer

from app.db.database import engine

"""
Создание класса для создания таблицы
"""

enrollment = Table(
    "enrollment",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("student.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("course.id"), primary_key=True),
)


class Course(Base):
    __tablename__ = "course"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))

    lessons: Mapped[list["Lesson"]] = relationship(back_populates="course")
    students: Mapped[list["Student"]] = relationship(
        secondary=enrollment, back_populates="courses"
    )


class Lesson(Base):
    __tablename__ = 'lesson'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    content: Mapped[str]
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"))

    course: Mapped["Course"] = relationship(back_populates="lessons")


class Student(Base):
    __tablename__ = 'student'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))

    courses: Mapped[list["Course"]] = relationship(
        secondary=enrollment, back_populates="students"
    )


with Session(autoflush=False, bind=engine) as db:
    beadweaving = Course(name="Beadweaving")
    macrame = Course(name="Macrame")

    pupa = Student(name="Pupa")
    lupa = Student(name="Lupa")

    lesson_1 = Lesson(name="Beadweaving for noobs")
    lesson_2 = Lesson(name="Beadweaving advanced")
    lesson_3 = Lesson(name="Macrame Basics")
    lesson_4 = Lesson(name="Macrameniacs")

    beadweaving.lessons = [lesson_1, lesson_2]
    macrame.lessons = [lesson_3, lesson_4]

    beadweaving.students = [pupa]
    macrame.students = [lupa]

    db.add_all([beadweaving, macrame])
    db.commit()
