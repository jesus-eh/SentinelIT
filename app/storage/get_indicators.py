from sqlalchemy import select
from models.indicator import Indicator

def get_indicators(db):

    consulta = select(Indicator)
    resultado = db.execute(consulta)
    indicadors = resultado.scalars().all()

    return indicadors

def get_indicatorsID(db, id):

    consulta = select(Indicator).where(Indicator.id == id)
    resultado = db.execute(consulta)
    indicadors = resultado.scarlars().one_or_none()

    return indicadors

def post_indicator(indicator, db):
    try:
        indicator_db = indicator(
            type=indicator.type,
            value=indicator.value,
            source=indicator.source,
            confidence=indicator.confidence,
            threat_type=indicator.threat_type,
            tags=indicator.tags
        )

        db.add(indicator_db)
        db.commit()
        db.refresh(indicator_db)

        return {"succes": "ok"}
    except Exception as e:
        return {"succes": "Error"}, {"msg" : f" Indicators no subido {e}"}
