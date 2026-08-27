from pydantic_settings import BaseSettings
from pathlib import Path


class Config(BaseSettings):
    frontend_dir: Path = Path(__file__).resolve().parents[1] / "frontend"
    secret_key: String = String("secret")
    algorithm = "HS256"
    token_expire_session = 60
    pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated=["bcrypt"])


config = Config()

DATABASE_URL = 'sqlite:///./lms.db'
