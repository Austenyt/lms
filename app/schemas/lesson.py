from pydantic import BaseModel
from typing import Optional

class LessonFind(BaseModel):
    id: int


class LessonCreate(BaseModel):
    name: str
    content: str


class LessonPatch(BaseModel):
    id: int
    name: Optional[str]
    content: Optional[str]
