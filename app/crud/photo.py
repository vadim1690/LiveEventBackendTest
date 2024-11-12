from sqlalchemy.orm import Session
from app.models.photo import Photo
from app.schemas.photo import PhotoCreate

def create_photo(db: Session, photo: PhotoCreate):
    db_photo = Photo(**photo.model_dump())
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo

def get_photos(db: Session):
    return db.query(Photo).all()

def get_photo(db: Session,photo_id:int):
    return db.query(Photo).filter(Photo.id == photo_id).first()
