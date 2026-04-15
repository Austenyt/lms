from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import Integer


class Course(Base):
    __tablename__ = "course"

    name: Mapped[str] = mapped_column(String(150))
    qty: Mapped[int] = mapped_column(Integer)
