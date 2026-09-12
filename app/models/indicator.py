from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, ConfigDict
from datetime import datetime

Base = declarative_base()

class Indicator(Base):
    __tablename__ = "indicators"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    value = Column(String, nullable=False)
    source = Column(String)
    first_seen = Column(DateTime)
    last_seen = Column(DateTime)
    confidence = Column(Float)
    risk_score = Column(Float)
    threat_type = Column(String)
    tags = Column(JSON)

# Modelo schema
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