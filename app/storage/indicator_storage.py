from sqlalchemy import select
from app.models.indicator import Indicator

# We collect all the indicators   
def get_indicators(db):

    consulta = select(Indicator)
    resultado = db.execute(consulta)
    indicadors = resultado.scalars().all()

    return indicadors

# Retrieve indicator by ID
def get_indicatorsID(db, id):

    consulta = select(Indicator).where(Indicator.id == id)
    resultado = db.execute(consulta)
    indicadors = resultado.scalars().one_or_none()

    return indicadors

# Uploading the indicators   
def post_indicator(indicator, db):
    try:
        indicator_db = Indicator(
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
        return {"succes": "Error", "msg" : f" Indicators no subido {e}"}

# Delete the indicator by id
def del_indicator(id, db):

    try:
        consulta = select(Indicator).where(Indicator.id == id)
        resultado = db.execute(consulta)
        indicador = resultado.scalars().one_or_none()
        if indicador:
            db.delete(indicador)
            db.commit()
            return {"succes" : "ok"}
        else:
            return {"succes": "Error"}

    except Exception as e:
        return {"succes": "Error", "msg" : f" Indicators no eliminado: {e}"}
