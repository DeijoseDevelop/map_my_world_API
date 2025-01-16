from abc import ABC, abstractmethod
from typing import List

from ..entities.review import LocationCategoryReview


class ILocationCategoryReviewRepository(ABC):

    @abstractmethod
    async def get_recommendations(self) -> List[LocationCategoryReview] | None:
        pass