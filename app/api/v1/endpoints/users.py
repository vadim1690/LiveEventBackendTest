# app/api/api_router.py
from fastapi import APIRouter, Depends, HTTPException,Form,File,UploadFile
from sqlalchemy.orm import Session
from app.crud.user import get_user, get_users, create_user
from app.dependencies.services import get_user_service
from app.schemas.photo import Photo
from app.schemas.user import UserCreate, UserResponse
from app.dependencies.database import get_db
from app.services.user_service import UserService

router = APIRouter()

@router.post("", response_model=UserResponse)
async def create_user(
    full_name: str = Form(...),
    email: str = Form(...),
    photo: UploadFile = File(...),  # Required file upload
    user_service: UserService = Depends(get_user_service),
):
    return user_service.create_user(user=UserCreate(name=full_name,email=email),photo=photo.file)

@router.get("", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, user_service: UserService = Depends(get_user_service)):
    return user_service.get_users(skip=skip, limit=limit)

@router.get("", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, user_service: UserService = Depends(get_user_service)):
    return user_service.get_users(skip=skip, limit=limit)


@router.get("/{user_id}/photos", response_model=list[Photo])
def get_user_photos(user_id: int, user_service: UserService = Depends(get_user_service)):
    photos = user_service.get_user_photos(user_id=user_id)
    if photos is None:
        raise HTTPException(status_code=404, detail="User not found or no photos available")
    return photos