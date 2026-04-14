from pydantic_settings import BaseSettings
from pathlib import Path


class Config(BaseSettings):
    frontend_dir: Path = Path(__file__).resolve().parents[1] / "frontend"


config = Config()
