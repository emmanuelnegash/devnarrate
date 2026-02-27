from fastapi import FastAPI
from src.core.config import settings
from src.core.logging import logger

app = FastAPI(title=settings.app_name)
logger.info("DevNarrate API started")