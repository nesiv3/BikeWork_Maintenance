# app/domain/repositories/maintenance_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.maintenance import Maintenance


class MaintenanceRepository(ABC):
    """Contrato que deben cumplir las implementaciones (Mongo, SQL, etc.)."""

    @abstractmethod
    def save(self, maintenance: Maintenance) -> None:
        """Persiste un mantenimiento nuevo."""
        ...

    @abstractmethod
    def update(self, maintenance: Maintenance) -> None:
        """Reemplaza el documento/registro completo (o aplica un patch)."""
        ...

    @abstractmethod
    def get_by_id(self, maintenance_id: str) -> Optional[Maintenance]:
        """Devuelve un mantenimiento o `None` si no existe."""
        ...

    @abstractmethod
    def list_by_store(self, store_id: int) -> List[Maintenance]:
        """Listado de mantenimientos por tienda (útil para dashboards)."""
        ...
