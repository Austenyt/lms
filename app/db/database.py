from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
Адрес для подключения к БД:
"""
DATABASE_URL = 'sqlite:///./lms.db'

"""
Создание движка для управления подключениями к БД:
Передаем адрес для подключения и дополнительные параметры - отключение проверки использования единого потока.
"""
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
"""
Создание локальной сессии подключения с помощью класса sessionmaker.
Передаем параметры отключение автоматического сохранения сессии, отключение автоматического сброса, привязывание сессии к движку.
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
