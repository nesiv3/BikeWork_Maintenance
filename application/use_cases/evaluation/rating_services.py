# app/service/rating_service.py

from domain.repositories.evaluation_repository import EvaluationRepository


class RatingService:
    def __init__(self, repository: EvaluationRepository):
        self.repository = repository

    def get_store_average(self, store_id: int) -> float:
        count = self.repository.get_average_rating_by_store(store_id)
        if count is None:
            return 0.0
        return count
