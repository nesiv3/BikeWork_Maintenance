from pymongo.collection import Collection
from domain.entities.maintenance import Maintenance


class MaintenanceRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def save(self, maintenance: Maintenance):
        self.collection.insert_one(maintenance.dict())

    def update(self, maintenance: Maintenance):
        self.collection.replace_one({"id": maintenance.id}, maintenance.dict())

    def get_by_id(self, maintenance_id: str) -> Maintenance:
        data = self.collection.find_one({"id": maintenance_id})
        return Maintenance(**data)
    
    def count_by_store(self, store_id: int) -> int:
        return self.collection.count_documents({"store_id": store_id})
