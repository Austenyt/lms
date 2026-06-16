from pydantic import BaseModel
from typing import Optional

class LessonFind(BaseModel):
    id: int


class LessonCreate(BaseModel):
    name: str
    content: str
    course_id: int


class LessonPatch(BaseModel):
    id: int
    name: Optional[str]
    content: Optional[str]
