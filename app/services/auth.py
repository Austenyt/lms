from passlib.context import CryptContext

from app.models.models import Student


class AuthService:
    def __init__(self):
        self.secret_key = "secret"
        self.algorithm = "HS256"
        self.token_expire_session = 60
        self.pwd_context = CryptContext(schemes=["bcrypt"])

    def register(self, username, password, session):
        existing = session.query(Student).where(Student.username == username)
        if existing:
            raise ValueError("Уже существует")
        hashed_password = self.pwd_context.hash(password)
        student = Student(username=username, hashed_password=hashed_password)
        session.add(student)
        session.commit()
        session.refresh(student)
        return student