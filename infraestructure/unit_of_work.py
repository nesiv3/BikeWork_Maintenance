import os
from dotenv import load_dotenv
from pymongo import MongoClient
from infraestructure.mongo.evaluation_repository import EvaluationRepository
from infraestructure.mongo.maintenance_repository import MaintenanceRepository

load_dotenv()  

mongo_uri = os.getenv("MONGO_URI")
mongo_db = os.getenv("MONGO_DB")

class UnitOfWork:
    def __init__(self, uri=mongo_uri, db_name=mongo_db):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.maintenance_repository = MaintenanceRepository(self.db["maintenance"])
        self.evaluation_repository = EvaluationRepository(self.db["evaluation"])

    def __enter__(self):
        # Aquí podrías iniciar una sesión/transaction si usas MongoDB >= 4.0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Aquí podrías manejar commit/rollback si usas transacciones
        self.client.close()