from pydantic import BaseModel


class CourseCreate(BaseModel):
    id: int
    name: str
    qty: int
