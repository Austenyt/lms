from pydantic import BaseModel, ConfigDict


class UserRegister(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str


class UserRegisterResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    first_name: str
    last_name: str
    username: str


class UserLogin(BaseModel):
    username: str
    password: str
