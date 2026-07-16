from datetime import datetime, timedelta
from sqlalchemy import select

from passlib.context import CryptContext

from app.models.models import Student
from jose import jwt, JWTError


class AuthService:
    def __init__(self):
        self.secret_key = "secret"
        self.algorithm = "HS256"
        self.token_expire_session = 60
        self.pwd_context = CryptContext(schemes=["bcrypt"])

    def register(self, username, password, session):
        existing = session.scalar(select(Student).where(Student.username == username))
        if existing:
            raise ValueError("Уже существует")
        hashed_password = self.pwd_context.hash(password)
        student = Student(username=username, hashed_password=hashed_password)
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

    def login(self, username, password, session):
        student = session.scalar(Student).where(Student.username == username)
        if not student:
            raise ValueError("Пользователь не зарегистрирован")

        if not self.pwd_context.verify(password, student.hashed_password):
            raise ValueError("Введенный пароль неверен")

        token = self._create_token(student.id)
        return token

    def _create_token(self, student_id):
        expire = datetime.utcnow() + timedelta(minutes=self.token_expire_session)
        payload = {
            'expire': expire,
            'sub': student_id,
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def _get_current_student(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload['sub']
        except JWTError:
            raise ValueError("Невалидный токен")

auth_service = AuthService()
