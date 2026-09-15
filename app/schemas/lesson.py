from pydantic import BaseModel, ConfigDict


class LessonFind(BaseModel):
    id: int


class LessonResponse(BaseModel):
    id: int
    name: str
    course_id: int


class LessonCreate(BaseModel):
    name: str
    content: str
    course_id: int


class LessonCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    course_id: int


class LessonPatch(BaseModel):
    id: int
    name: str
    content: str


class LessonPatchResponse(BaseModel):
    id: int
    name: str
