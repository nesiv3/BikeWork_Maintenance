from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class MaintenanceEvent(BaseModel):
    event_type: str
    timestamp: datetime
    details: dict


class Maintenance(BaseModel):
    id: str
    user_id: str
    store_id: int
    maintenance_type_id: int
    status: str
    entry_date: datetime
    out_date: Optional[datetime]
    maintenance_observation: str
    events: List[MaintenanceEvent]

    def add_event(self, event: MaintenanceEvent):
        self.events.append(event)
        self.status = self._map_event_to_status(event.event_type)

    def _map_event_to_status(self, event_type: str) -> str:
        mapping = {
            "MaintenanceRequested": "ingress",
            "MaintenanceInService": "service",
            "MaintenanceCompleted": "end_serv",
            "MaintenanceDelivered": "delivered"
        }
        return mapping.get(event_type, self.status)