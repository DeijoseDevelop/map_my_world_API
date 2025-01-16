from typing import Annotated

from fastapi import Query
from sqlmodel import Session, select

from app.domain.entities.e_category import Category
from app.domain.repositories.r_category import ICategoryRepository
from app.infrastructure.models import CategoryModel


class DBCategoryRepository(ICategoryRepository):
    def __init__(self, session: Session):
        self.session = session

    async def create(self, category: Category) -> Category:
        db_category = CategoryModel(
            name=category.name, description=category.description
        )

        self.session.add(db_category)
        self.session.commit()
        self.session.refresh(db_category)

        return Category(
            id=db_category.id,
            name=db_category.name,
            description=db_category.description,
            created_at=db_category.created_at,
        )

    async def findAll(
        self,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
    ):
        categories = self.session.exec(
            select(CategoryModel).offset(offset).limit(limit)
        ).all()

        return categories