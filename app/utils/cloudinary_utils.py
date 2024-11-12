# app/utils/cloudinary_utils.py
import cloudinary
import cloudinary.uploader

def upload_photo_to_cloudinary(file) -> str:
    """Uploads a file to Cloudinary and returns the URL."""
    result = cloudinary.uploader.upload(file,resource_type="image")
    return result['url']
