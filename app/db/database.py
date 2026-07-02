from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL


engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = session_maker()
    try:
        yield session
    finally:
        session.close()
