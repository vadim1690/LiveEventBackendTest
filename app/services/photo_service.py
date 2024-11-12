# app/services/photo_service.py
import face_recognition
import numpy as np
from sqlalchemy.orm import Session
from app.schemas.photo import PhotoCreate, Photo
from app.crud.photo import create_photo, get_photos, get_photo
from app.utils.cloudinary_utils import upload_photo_to_cloudinary
from app.utils.face_encoding_utils import encode_face
from app.exceptions import NoFaceDetectedException, NoMatchingPhotosFoundException
from typing import List
from app.config.logger_config import get_logger

logger = get_logger()

class PhotoService:
    def __init__(self, db: Session):
        self.db = db

    def upload_photo(self, photo_file) -> PhotoCreate:
        file_bytes = photo_file.read()  # Read the file's content
        encoding = encode_face(photo_file)
        if encoding is None:
            logger.error("No face detected in the uploaded photo.")
            raise NoFaceDetectedException("No face detected in the photo")
        file_url = upload_photo_to_cloudinary(file_bytes)
        encoding_str = ",".join(map(str, encoding))
        db_photo = PhotoCreate(url=file_url, encoding=encoding_str)
        return create_photo(self.db, db_photo)

    def search_photo(self, photo) -> List[Photo]:
        encoding = encode_face(photo)
        if encoding is None:
            logger.error("No face detected in the photo.")
            raise NoFaceDetectedException("No face detected in the photo")
        return self.search_encoding(encoding)

    def search_encoding(self, encoding_list) -> List[Photo]:
        stored_photos = get_photos(self.db)
        matches = []
        # Convert encoding_list to a NumPy array
        encoding_to_check = np.array(encoding_list, dtype=float)

        for stored_photo in stored_photos:
            # Convert stored encoding to a NumPy array
            stored_encoding = np.array(list(map(float, stored_photo.encoding.split(','))), dtype=float)

            # Pass NumPy arrays to compare_faces
            result = face_recognition.compare_faces([stored_encoding], encoding_to_check)

            if result[0]:  # If there's a match
                matches.append(stored_photo)

        if not matches:
            logger.info("No matching photos found for the uploaded photo.")
            raise NoMatchingPhotosFoundException("No matching photos found")

        return matches

    def get_photos(self):
        return get_photos(self.db)

    def get_photo(self,photo_id:int):
        return get_photo(self.db,photo_id)