from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from app.config import Settings, get_settings
from app.application.api.routes import ro_category, ro_location, ro_review
from app.infrastructure.database import create_db_and_tables


@asynccontextmanager
async def lifespan(_app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title="Map My World API",
    description="API for managing locations, categories, and exploration recommendations",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/health-check")
def health_check(settings: Settings = Depends(get_settings)):
    return {
        "running": True,
        "environment": settings.environment,
        "testing": settings.testing,
    }


app.include_router(ro_category.router, tags=["Categories"])
app.include_router(ro_location.router, tags=["Locations"])
app.include_router(ro_review.router, tags=["Recommendations"])
