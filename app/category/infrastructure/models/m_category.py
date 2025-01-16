from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from sqlmodel import Field, Relationship, SQLModel

from app.review.infrastructure.models.m_location_category_review import LocationCategoryReviewModel


class CategoryModel(SQLModel, table=True):
    __tablename__ = "categories"

    id: str | None = Field(
        default_factory=lambda: str(uuid4()), primary_key=True, index=True, unique=True
    )
    name: str = Field(unique=True, nullable=False, index=True)
    description: str = Field(nullable=False)
    created_at: Optional[str] = Field(default=datetime.now().strftime("%Y-%m-%d"))

    # Relationship
    reviews: List[LocationCategoryReviewModel] = Relationship(back_populates="category")