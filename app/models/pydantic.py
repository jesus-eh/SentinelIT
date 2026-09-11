from pydantic import BaseModel, ConfigDict
from datetime import datetime

class IndicatorCreate(BaseModel):
    type: str
    value: str
    source: str | None = None
    confidence: float | None = None
    threat_type: str | None = None
    tags: list[str] = []


class IndicatorResponse(BaseModel):
    id: int
    type: str
    value: str
    source: str | None = None
    first_seen: datetime | None = None
    last_seen: datetime | None = None
    confidence: float | None = None
    risk_score: float | None = None
    threat_type: str | None = None
    tags: list[str] = []

    model_config = ConfigDict(from_attributes=True)