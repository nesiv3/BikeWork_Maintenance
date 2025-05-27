from fastapi import APIRouter, Depends
from application.use_cases.maintenance.create_maintenance import create_maintenance
from pymongo import MongoClient
from fastapi import APIRouter, Depends, Query
from application.use_cases.maintenance.maintenance_service import MaintenanceService
from infraestructure.unit_of_work import UnitOfWork
from utils.cache import redis_cache

router = APIRouter()

@router.post("/maintenance")
def new_maintenance(data: dict):
    with UnitOfWork() as uow:
        maintenance = create_maintenance(data)
        uow.maintenance_repository.save(maintenance)
        return maintenance
    
@router.get("/maintenance/count_by_store/{store_id}")
@redis_cache("/maintenance/count_by_store/{store_id}", expire=86400)
def count_maintenance_by_store(store_id: int):
    with UnitOfWork() as uow:
        service = MaintenanceService(uow.maintenance_repository)
        count = service.list_by_store(store_id)
        
        return {"store_id": store_id, "maintenance_count": count}