import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api_router import api_router
from app.dependencies.database import engine, Base

from app.config.logger_config import get_logger

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = get_logger()

# Initialize Database Tables
logger.info("Creating database tables...")
Base.metadata.create_all(bind=engine)
logger.info("Database tables created.")

# Create FastAPI app
logger.info("Starting FastAPI application...")
app = FastAPI(
    title="Test API",
    description="API documentation for Test API",
    version="1.0.0")
logger.info("FastAPI application created.")

logger.info("Setting CORS")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logger.info("CORS Setting finished")

# Register Routes
logger.info("Registering routes...")
app.include_router(api_router, prefix="/api/v1")
logger.info("Routes registered.")
