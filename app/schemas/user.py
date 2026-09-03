from pydantic import BaseModel


class UserFind(BaseModel):
    id: int


class UserCreate(BaseModel):
    first_name: str
    last_name: str


class UserPatch(BaseModel):
    id: int
    first_name: str | None = None
    last_name: str | None = None


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    courses: list


class Enroll(BaseModel):
    course_id: int
    user_id: int
