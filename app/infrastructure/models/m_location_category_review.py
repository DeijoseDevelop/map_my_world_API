from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from sqlmodel import Field, Relationship, SQLModel


class LocationCategoryReviewModel(SQLModel, table=True):
    __tablename__ = "location_category_reviewed"

    id: str = Field(primary_key=True, index=True, unique=True)
    location_id: str = Field(foreign_key="locations.id")
    category_id: str = Field(foreign_key="categories.id")
    last_reviewed_at: Optional[str] = Field(default=None, nullable=True)

    # Relationships
    location: "LocationModel" = Relationship(back_populates="reviews")
    category: "CategoryModel" = Relationship(back_populates="reviews")