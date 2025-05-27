# application/use_cases/create_maintenance.py

from domain.entities.maintenance import Maintenance, MaintenanceEvent
from datetime import datetime
from uuid import uuid4


def create_maintenance(data: dict) -> Maintenance:
    return Maintenance(
        id=f"mnt-{datetime.utcnow().strftime('%Y%m%d')}-{str(uuid4())[:4]}",
        user_id=data["user_id"],
        store_id=data["store_id"],
        maintenance_type_id=data["maintenance_type_id"],
        status="ingress",
        entry_date=datetime.utcnow(),
        out_date=None,
        maintenance_observation=data["maintenance_observation"],
        events=[
            MaintenanceEvent(
                event_type="MaintenanceRequested",
                timestamp=datetime.utcnow(),
                details={"created_by": data["user_id"]}
            )
        ]
    )
