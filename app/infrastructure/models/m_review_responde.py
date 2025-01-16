from typing import Optional

from sqlmodel import SQLModel


class ReviewResponse(SQLModel):
    id: str
    last_reviewed_at: Optional[str]
    location: LocationModel
    category: CategoryModel

    class Config:
        from_attributes = True