# app/api/router.py

from fastapi import APIRouter, Depends, HTTPException
from pymongo import MongoClient
from domain.repositories.evaluation_repository import EvaluationRepository
from application.use_cases.evaluation.rating_services import RatingService
from infraestructure.unit_of_work import UnitOfWork
from utils.cache import redis_cache

router = APIRouter()

def get_service():
    with UnitOfWork() as uow:
        return RatingService(uow.evaluation_repository)

@router.get("/store/{store_id}/average-rating")
def get_average_rating(store_id: int):
    with UnitOfWork() as uow:
        service = RatingService(uow.evaluation_repository)
        avg = service.get_store_average(store_id)
        if avg is None:
            avg=0;
        return {"store_id": store_id, "average_rating": round(avg, 2)}
