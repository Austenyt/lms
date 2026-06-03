from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL

"""
Создание движка для управления подключениями к БД:
Передаем адрес для подключения и дополнительные параметры - отключение проверки использования единого потока.
"""
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
"""
Создание локальной сессии подключения с помощью класса sessionmaker.
Передаем параметры отключение автоматического сохранения сессии, отключение автоматического сброса, привязывание сессии к движку.
"""
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = session_maker()
    try:
        yield session
    finally:
        session.close()


# def hello():
#     yield 'Hello'
#     yield 'World'
#     yield 'Bro'
#
#
# g = hello()
# # print(next(g))
# for elem in g:
#     print(elem)
