from abc import ABC, abstractmethod
from typing import List

from ..entities.e_location import Location


class ILocationRepository(ABC):

    @abstractmethod
    async def create(self, location: Location) -> Location:
        pass

    @abstractmethod
    async def findAll(self, offset: int = 0, limit: int = 100) -> List[Location] | None:
        pass