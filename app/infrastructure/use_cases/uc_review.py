from typing import List

from app.domain.entities.review import LocationCategoryReview
from app.domain.repositories.r_review import ILocationCategoryReviewRepository
from app.domain.use_cases.uc_base import UseCase


class GetRecommendationsUseCase(UseCase):
    def __init__(self, review_repository: ILocationCategoryReviewRepository):
        self.review_repository = review_repository

    async def execute(self, limit: int = 10) -> List[LocationCategoryReview]:
        return await self.review_repository.get_recommendations(limit)