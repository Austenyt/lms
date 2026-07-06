from pydantic import BaseModel


class StudentFind(BaseModel):
    id: int


class StudentCreate(BaseModel):
    first_name: str
    last_name: str


class StudentPatch(BaseModel):
    id: int
    first_name: str | None = None
    last_name: str | None = None


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    courses: list


class Enroll(BaseModel):
    course_id: int
    student_id: int
