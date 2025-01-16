from abc import ABC, abstractmethod
from typing import List

from ..entities.e_category import Category


class ICategoryRepository(ABC):

    @abstractmethod
    async def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    async def findAll(self, offset: int = 0, limit: int = 100) -> List[Category] | None:
        pass