from app.domain.entities.e_location import Location
from app.domain.repositories.r_location import ILocationRepository
from app.domain.use_cases.uc_base import UseCase


class CreateLocationUseCase(UseCase):
    def __init__(self, location_repository: ILocationRepository):
        self.location_repository = location_repository

    async def execute(self, location_data: Location) -> Location:
        return await self.location_repository.create(location_data)


class GetAllLocationsUseCase(UseCase):
    def __init__(self, location_repository: ILocationRepository):
        self.location_repository = location_repository

    async def execute(self, offset: int = 0, limit: int = 100) -> Location:
        return await self.location_repository.all(offset, limit)