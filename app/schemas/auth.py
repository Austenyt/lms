from pydantic import BaseModel


class UserRegister(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
