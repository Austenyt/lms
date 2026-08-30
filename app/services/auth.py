from datetime import datetime, timedelta
from sqlalchemy import select

from app.models.models import Student
from app.config import config
from jose import jwt, JWTError


class AuthService:
    def __init__(self):
        self.secret_key = config.secret_key
        self.algorithm = config.algorithm
        self.token_expire_session = config.token_expire_session
        self.pwd_context = config.pwd_context

    def register(self, first_name, last_name, username, password, session):
        existing = session.scalar(select(Student).where(Student.username == username))
        if existing:
            raise ValueError("Уже существует")
        if len(password) < 8 or len(password) > 12:
            raise ValueError("Пароль не соответствует требованиям")
        hashed_password = self.pwd_context.hash(password)
        student = Student(
            first_name=first_name,
            last_name=last_name,
            username=username,
            hashed_password=hashed_password
        )
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

    def login(self, username, password, session):
        student = session.scalar(select(Student).where(Student.username == username))
        if not student:
            raise ValueError("Пользователь не зарегистрирован")

        if not self.pwd_context.verify(password, student.hashed_password):
            raise ValueError("Введенный пароль неверен")

        token = self._create_token(student.id)
        return token

    def _create_token(self, student_id):
        expire = datetime.utcnow() + timedelta(minutes=self.token_expire_session)
        payload = {
            'exp': expire,
            'sub': str(student_id),
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def get_current_student(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload['sub']
        except JWTError:
            raise ValueError("Невалидный токен")


auth_service = AuthService()
