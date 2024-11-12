# app/crud/user.py
import logging
from sqlalchemy.orm import Session

from app.models.photo import Photo
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    # Use a join to include the photo URL in each user's data
    users_with_photos = (
        db.query(User, Photo.url.label("photo_url"))
        .outerjoin(Photo, User.photo_id == Photo.id)
        .order_by(User.id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    # Transform each tuple into a UserResponse-compatible dictionary
    return [
        UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            photo_url=photo_url
        )
        for user, photo_url in users_with_photos
    ]


def create_user(db: Session, user: UserCreate,photo_id:int):
    db_user = User(name=user.name, email=user.email,photo_id=photo_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
