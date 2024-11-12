from sqlalchemy import Column, Integer, String,Text
from app.dependencies.database import Base

class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(255), unique=True, index=True)
    encoding = Column(Text)