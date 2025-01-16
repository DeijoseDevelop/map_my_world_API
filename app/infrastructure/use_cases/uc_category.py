from app.domain.entities.e_category import Category
from app.domain.repositories.r_category import ICategoryRepository
from app.domain.use_cases.uc_base import UseCase


class CreateCategoryUseCase(UseCase):
    def __init__(self, category_repository: ICategoryRepository):
        self.category_repository = category_repository

    async def execute(self, category_data: Category) -> Category:
        return await self.category_repository.create(category_data)


class GetAllCategoriesUseCase(UseCase):
    def __init__(self, category_repository: ICategoryRepository):
        self.category_repository = category_repository

    async def execute(self, offset: int = 0, limit: int = 100) -> Category:
        return await self.category_repository.findAll(offset, limit)