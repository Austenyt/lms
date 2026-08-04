from pydantic import BaseModel


class StudentRegister(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str


class StudentLogin(BaseModel):
    username: str
    password: str
