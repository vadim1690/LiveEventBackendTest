# app/controllers/photo_controller.py
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from app.dependencies.services import get_photo_service
from app.schemas.photo import Photo
from app.services.photo_service import PhotoService
from app.exceptions import NoFaceDetectedException, NoMatchingPhotosFoundException

router = APIRouter()

@router.post("/upload")
async def upload_photo(photo: UploadFile = File(...), photo_service: PhotoService = Depends(get_photo_service)):
    try:
        return photo_service.upload_photo(photo.file)
    except NoFaceDetectedException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("", response_model=list[Photo])
async def get_photos(photo_service: PhotoService = Depends(get_photo_service)):
    try:
        return photo_service.get_photos()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/search")
async def search_photo(photo: UploadFile = File(...), photo_service: PhotoService = Depends(get_photo_service)):
    try:
        matches = photo_service.search_photo(photo.file)
        return {"matches": matches}
    except NoFaceDetectedException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except NoMatchingPhotosFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
