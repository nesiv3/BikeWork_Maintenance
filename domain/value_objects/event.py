# app/domain/value_objects/event.py

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Dict, Any


class Event(BaseModel):
    """Representa un hecho inmutable en el tiempo."""
    event_type: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    details: Dict[str, Any]

    class Config:
        frozen = True          # inmutabilidad ↔️ event sourcing
        orm_mode = True        # por si usas ODMs/ORMs
