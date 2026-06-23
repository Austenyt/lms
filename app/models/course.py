from app.db.base import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey
from sqlalchemy import Integer

"""
Создание класса для создания таблицы
"""


class Course(Base):
    __tablename__ = "course"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))

    lessons: Mapped[list["Lesson"]] = relationship(back_populates="course")


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
