# app/service/rating_service.py


from domain.repositories.maintenance_repository import MaintenanceRepository


class MaintenanceService:
    def __init__(self, repository: MaintenanceRepository):
        self.repository = repository

    def list_by_store(self, store_id: int) -> float:
        listStore = self.repository.list_by_store(store_id)      
        return listStore
    


