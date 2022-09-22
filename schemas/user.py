from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    cedula: str
    name: str
    lastname: str
    age: str
    email: str
    gender: str
    password: str
