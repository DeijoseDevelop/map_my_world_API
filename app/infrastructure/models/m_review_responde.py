from typing import Optional

from sqlmodel import SQLModel


from app.infrastructure.models.m_category import CategoryModel
from app.infrastructure.models.m_location import LocationModel


class ReviewResponse(SQLModel):
    id: str
    last_reviewed_at: Optional[str]
    location: LocationModel
    category: CategoryModel

    class Config:
        from_attributes = True