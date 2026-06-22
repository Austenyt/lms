from pydantic import BaseModel


class CourseFind(BaseModel):
    id: int


class CourseCreate(BaseModel):
    name: str


class CoursePatch(BaseModel):
    id: int
    name: str = None
