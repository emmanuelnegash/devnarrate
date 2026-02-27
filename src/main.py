from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.core.config import settings
from src.core.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("DevNarrate API starting...")
    yield
    logger.info("DevNarrate API shutting down...")


app = FastAPI(title=settings.app_name, debug=getattr(settings, "debug", False), lifespan=lifespan)


@app.get("/health", tags=["system"])
async def health():
    return {"status": "ok", "app": settings.app_name}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Includes traceback for easier debugging
    logger.exception("Unhandled error", extra={"path": str(request.url.path), "method": request.method})
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})