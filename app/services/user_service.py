# app/services/photo_service.py
from idlelib.iomenu import encoding

from sqlalchemy.orm import Session

from app.crud.user import create_user, get_users, get_user
from app.schemas.photo import Photo
from app.schemas.user import UserResponse, UserCreate,UserExtendedResponse
from app.services.photo_service import PhotoService

from typing import List
from app.config.logger_config import get_logger

logger = get_logger()


class UserService:
    def __init__(self, db: Session, photo_service: PhotoService):
        self.db = db
        self.photo_service = photo_service

    def create_user(self, user: UserCreate, photo) -> UserResponse:
        #upload photo to storage and create record
        created_photo = self.photo_service.upload_photo(photo)

        #create user
        created_user = create_user(self.db, user, created_photo.id)

        return UserResponse(id=created_user.id, name=created_user.name, email=created_user.email,
                            photo_url=created_photo.url)

    def get_users(self, skip: int = 0, limit: int = 10) -> List[UserResponse]:
        return get_users(self.db, skip, limit)

    def get_user(self, user_id:int) -> UserExtendedResponse:
        return get_user(self.db, user_id)

    def get_user_photos(self,user_id:int) -> List[Photo]:
        #get user by id
        user = self.get_user(user_id)

        #get photo encoding by photo id from user
        photo = self.photo_service.get_photo(photo_id=user.photo_id)
        # perform search
        encoding_list = list(map(float, photo.encoding.split(',')))
        return self.photo_service.search_encoding(encoding_list)