from typing import Annotated, List

from fastapi import APIRouter, Depends, Query

from app.common.infrastructure.dependencies import get_review_repository
from app.review.infrastructure.models.m_review_responde import ReviewResponse
from app.review.application.uc_review import GetRecommendationsUseCase

router = APIRouter()


@router.get("/recommendations/", response_model=List[ReviewResponse])
async def get_recommendations(
    limit: Annotated[int, Query(le=100)] = 100,
    use_case: GetRecommendationsUseCase = Depends(
        lambda: GetRecommendationsUseCase(get_review_repository())
    ),
):
    return await use_case.execute(limit)