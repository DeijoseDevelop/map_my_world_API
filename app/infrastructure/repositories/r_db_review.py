from datetime import datetime, timedelta

from sqlmodel import Session, or_, select

from app.domain.repositories.r_review import ILocationCategoryReviewRepository
from app.infrastructure.models.models import LocationCategoryReviewModel


class DBLocationCategoryReviewRepository(ILocationCategoryReviewRepository):
    def __init__(self, session: Session):
        self.session = session

    async def get_recommendations(
        self,
        limit: int = 10,
    ):
        """
        Get 10 location-category combinations that need review, prioritizing those never reviewed
        and those not reviewed in the last 30 days.
        """

        # Subquery to get all reviewed combinations
        thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

        needs_review = self.session.exec(
            select(LocationCategoryReviewModel)
            .where(
                or_(
                    LocationCategoryReviewModel.last_reviewed_at.is_(None),
                    LocationCategoryReviewModel.last_reviewed_at == "",
                    LocationCategoryReviewModel.last_reviewed_at < thirty_days_ago,
                )
            )
            .join(LocationCategoryReviewModel.location)
            .join(LocationCategoryReviewModel.category)
            .order_by(
                LocationCategoryReviewModel.last_reviewed_at.is_(None).desc(),
                LocationCategoryReviewModel.last_reviewed_at.asc(),
            )
            .limit(limit)
        ).all()

        return needs_review