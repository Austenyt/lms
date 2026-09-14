from pydantic import BaseModel


class UserFind(BaseModel):
    id: int


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    courses: list


class Enroll(BaseModel):
    course_id: int
    user_id: int
