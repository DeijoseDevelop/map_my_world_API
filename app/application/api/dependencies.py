from app.infrastructure.database import get_session
from app.infrastructure.repositories.r_db_category import (
    DBCategoryRepository,
)
from app.infrastructure.repositories.r_db_location import (
    DBLocationRepository,
)
from app.infrastructure.repositories.r_db_review import (
    DBLocationCategoryReviewRepository,
)


def get_location_repository():
    return DBLocationRepository(next(get_session()))


def get_category_repository():
    return DBCategoryRepository(next(get_session()))


def get_review_repository():
    return DBLocationCategoryReviewRepository(next(get_session()))