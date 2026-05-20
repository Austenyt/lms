from pydantic import BaseModel


class CourseFind(BaseModel):
    id: int


class CourseCreate(BaseModel):
    name: str
    qty: int


class CoursePatch(BaseModel):
    id: int
    name: str = None
    qty: int = None
