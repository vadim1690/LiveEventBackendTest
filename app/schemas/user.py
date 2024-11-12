# app/schemas/user.py
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    photo_url:str

class UserExtendedResponse(UserResponse):
    photo_id:int

    class Config:
        orm_mode = True  # Allows SQLAlchemy models to return as Pydantic schemas
