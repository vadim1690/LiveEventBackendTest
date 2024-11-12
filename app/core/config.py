# app/core/config.py
import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import cloudinary



class Settings(BaseSettings):
    database_url: str  # No os.getenv(), directly declare as a field
    cloudinary_cloud_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str


    class Config:
        env_file = ".env"


settings = Settings()

# Cloudinary configuration
cloudinary.config(
    cloud_name=settings.cloudinary_cloud_name,
    api_key=settings.cloudinary_api_key,
    api_secret=settings.cloudinary_api_secret
)