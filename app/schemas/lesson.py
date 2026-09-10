from pydantic import BaseModel


class LessonFind(BaseModel):
    id: int


class LessonCreate(BaseModel):
    name: str | None = None
    content: str | None = None
    course_id: int


class LessonPatch(BaseModel):
    id: int
    name: str | None = None
    content: str | None = None
