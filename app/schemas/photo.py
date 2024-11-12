from pydantic import BaseModel

class PhotoBase(BaseModel):
    url: str

class PhotoCreate(PhotoBase):
    encoding: str

class Photo(PhotoBase):
    id: int

    class Config:
        orm_mode = True
