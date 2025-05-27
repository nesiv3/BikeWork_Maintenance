# app/service/rating_service.py

from domain.repositories.evaluation_repository import EvaluationRepository


class RatingService:
    def __init__(self, repository: EvaluationRepository):
        self.repository = repository

    def get_store_average(self, store_id: int) -> float:
        return self.repository.get_average_rating_by_store(store_id)
