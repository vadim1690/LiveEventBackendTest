# app/models/user.py
from sqlalchemy import Column, Integer, String, ForeignKey, Unicode
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Unicode(120), index=True)
    email = Column(String(50), unique=True, index=True)
    # Foreign key to associate a photo with the user
    photo_id = Column(Integer, ForeignKey("photos.id"))
    # Relationship to allow accessing the photo as an attribute
    photo = relationship("Photo")
