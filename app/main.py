from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from app.config import Settings, get_settings

app = FastAPI(
    title="Map My World API",
    description="API for managing locations, categories, and exploration recommendations",
    version="1.0.0",
)


@app.get("/health-check")
def health_check(settings: Settings = Depends(get_settings)):
    return {
        "running": True,
        "environment": settings.environment,
        "testing": settings.testing,
    }