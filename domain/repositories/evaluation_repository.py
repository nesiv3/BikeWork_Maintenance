# app/domain/repositories/maintenance_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.maintenance import Maintenance


class EvaluationRepository(ABC):
    """Contrato que deben cumplir las implementaciones (Mongo, SQL, etc.)."""

    @abstractmethod
    def get_average_rating_by_store(self, store_id: int) -> Optional[float]:
        """Persiste un mantenimiento nuevo."""
        ...
