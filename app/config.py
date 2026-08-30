from pydantic_settings import BaseSettings
from pathlib import Path
from passlib.context import CryptContext


class Config(BaseSettings):
    frontend_dir: Path = Path(__file__).resolve().parents[1] / "frontend"
    secret_key: str = "secret"
    algorithm: str = "HS256"
    token_expire_session: int = 60
    pwd_context: CryptContext = CryptContext(schemes=["argon2", "bcrypt"], deprecated=["bcrypt"])


config = Config()

DATABASE_URL = 'sqlite:///./lms.db'
