from app.db.base import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy import Integer


enrollment = Table(
    "enrollment",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("student.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("course.id"), primary_key=True),
)

ownership = Table(
    "ownership",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("student.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("course.id"), primary_key=True),
)

class Course(Base):
    __tablename__ = "course"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))
    owner_id: Mapped[int] = mapped_column(ForeignKey('student.id'))

    lessons: Mapped[list["Lesson"]] = relationship(back_populates="course", cascade="all, delete-orphan", passive_deletes=True)
    students: Mapped[list["Student"]] = relationship(
        secondary=enrollment, back_populates="courses"
    )
    owner: Mapped["Student"] = relationship(
        secondary=ownership, back_populates='courses'
    )


class Lesson(Base):
    __tablename__ = 'lesson'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    content: Mapped[str]
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id", ondelete="CASCADE"))

    course: Mapped["Course"] = relationship(back_populates="lessons")


class Student(Base):
    __tablename__ = 'student'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str]

    courses: Mapped[list["Course"]] = relationship(
        secondary=enrollment, back_populates="students"
    )
    courses_ownership: Mapped[list["Course"]] = relationship(
        secondary=ownership, back_populates="students"
    )

