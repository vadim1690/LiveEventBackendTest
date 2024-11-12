
from fastapi import Depends
from app.dependencies.database import get_db
from app.services.photo_service import PhotoService
from sqlalchemy.orm import Session

from app.services.user_service import UserService


def get_photo_service(db: Session = Depends(get_db)) -> PhotoService:
    return PhotoService(db)

def get_user_service(db: Session = Depends(get_db),photo_service: PhotoService = Depends(get_photo_service)) -> UserService:
    return UserService(db,photo_service)
