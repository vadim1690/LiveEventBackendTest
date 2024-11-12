# app/api/v1/api_router.py
from fastapi import APIRouter
from app.api.v1.endpoints import users,photos

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(photos.router, prefix="/photos", tags=["photos"])
