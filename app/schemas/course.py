from pydantic import BaseModel


class CourseFind(BaseModel):
    id: int


class CourseFindResponse(BaseModel):
    id: int
    name: str
    owner_id: int
    lessons: list


class CourseCreate(BaseModel):
    name: str


class CoursePatch(BaseModel):
    id: int
    name: str
