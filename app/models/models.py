from app.db.base import Base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy import Integer


enrollment = Table(
    "enrollment",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("course.id"), primary_key=True),
)


class Course(Base):
    __tablename__ = "course"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    lessons: Mapped[list["Lesson"]] = relationship(back_populates="course", cascade="all, delete-orphan")
    users: Mapped[list["User"]] = relationship(
        secondary=enrollment, back_populates="courses"
    )
    owner: Mapped["User"] = relationship(
        back_populates='owned_course'
    )


class Lesson(Base):
    __tablename__ = 'lesson'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    content: Mapped[str]
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id", ondelete="CASCADE"))

    course: Mapped["Course"] = relationship(back_populates="lessons")


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str]

    courses: Mapped[list["Course"]] = relationship(
        secondary=enrollment, back_populates="users"
    )

    owned_course: Mapped[list["Course"]] = relationship(
        back_populates="owner"
    )
