from pydantic import BaseModel, ConfigDict

from app.config import Config


class CourseFind(BaseModel):
    id: int


class CourseFindResponse(BaseModel):
    id: int
    name: str
    owner_id: int
    lessons: list


class CourseCreate(BaseModel):
    name: str


class CourseCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


class CoursePatch(BaseModel):
    id: int
    name: str | None = None
