from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import Integer

"""
Создание класса для создания таблицы
"""


class Course(Base):
    """
    Создание таблицы в БД
    """
    __tablename__ = "course"
    """
    Задание полей таблицы с описанием типов и атрибутов
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))
    qty: Mapped[int] = mapped_column(Integer)
