from pydantic import BaseModel

class StudentRegister(BaseModel):
    username: str
    password: str


class StudentLogin(BaseModel):
    username: str
    password: str
