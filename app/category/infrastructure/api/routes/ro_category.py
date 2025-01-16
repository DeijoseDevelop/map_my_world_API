from typing import Annotated

from fastapi import APIRouter, Depends, Query

from app.category.domain.entities.e_category import Category
from app.common.infrastructure.dependencies import get_category_repository
from app.category.application.uc_category import CreateCategoryUseCase, GetAllCategoriesUseCase

router = APIRouter()


@router.post("/categories/", response_model=Category)
async def create_category(
    category: Category,
    use_case: CreateCategoryUseCase = Depends(
        lambda: CreateCategoryUseCase(get_category_repository())
    ),
):
    return await use_case.execute(category)


@router.get("/categories/")
async def get_categories(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    use_case: GetAllCategoriesUseCase = Depends(
        lambda: GetAllCategoriesUseCase(get_category_repository())
    ),
):
    return await use_case.execute(offset, limit)