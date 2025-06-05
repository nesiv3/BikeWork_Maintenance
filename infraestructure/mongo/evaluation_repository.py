# app/repository/evaluation_repository.py

from pymongo.collection import Collection
from typing import Optional


class EvaluationRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def get_average_rating_by_store(self, store_id: int) -> Optional[float]:
        pipeline = [
            {"$match": {"store_id": store_id, "status": "active"}},
            {"$group": {"_id": "$store_id", "average_rating": {"$avg": "$rating"}}}
        ]
        result = list(self.collection.aggregate(pipeline))
        print(self.collection)
        return result[0]["average_rating"] if result else None
