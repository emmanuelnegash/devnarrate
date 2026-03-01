from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.core.config import settings
from src.core.logging import logger

from src.infrastructure.database.session import engine
from src.infrastructure.database.models import Base

from src.interfaces.api.routes import dev_test


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("DevNarrate API starting...")

    # Create database tables on startup
    Base.metadata.create_all(bind=engine)

    yield

    logger.info("DevNarrate API shutting down...")


app = FastAPI(
    title=settings.app_name,
    debug=getattr(settings, "debug", False),
    lifespan=lifespan,
)

# Include routers
app.include_router(dev_test.router)


@app.get("/health", tags=["system"])
async def health():
    return {"status": "ok", "app": settings.app_name}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(
        "Unhandled error",
        extra={"path": str(request.url.path), "method": request.method},
    )
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})