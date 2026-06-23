from pydantic import BaseModel
from typing import Optional


class StudentFind(BaseModel):
    id: int

class StudentCreate(BaseModel):
    first_name: str
    last_name: str

class StudentPatch(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
