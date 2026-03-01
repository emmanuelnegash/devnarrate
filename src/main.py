from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.concurrency import run_in_threadpool

from src.core.config import settings
from src.core.logging import logger
from src.infrastructure.database.models import Base
from src.infrastructure.database.session import engine
from src.interfaces.api.routes import dev_test


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("DevNarrate API starting...")

    # Only auto-create tables in dev/test scenarios.
    # (Prefer migrations in production)
    auto_create = bool(getattr(settings, "db_auto_create_tables", False))
    if auto_create:
        logger.info("Auto-creating database tables (db_auto_create_tables=True)")
        await run_in_threadpool(Base.metadata.create_all, bind=engine)

    yield

    logger.info("DevNarrate API shutting down...")


app = FastAPI(
    title=getattr(settings, "app_name", "DevNarrate"),
    debug=bool(getattr(settings, "debug", False)),
    lifespan=lifespan,
)

# Include routers
app.include_router(dev_test.router)


@app.get("/health", tags=["system"])
async def health() -> dict[str, Any]:
    return {"status": "ok", "app": getattr(settings, "app_name", "DevNarrate")}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # In debug, let FastAPI/Starlette display the default debug error page
    if bool(getattr(settings, "debug", False)):
        raise exc

    logger.exception(
        "Unhandled error",
        extra={"path": str(request.url.path), "method": request.method},
    )
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})