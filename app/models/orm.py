from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.orm import declarative_base

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