from sqlalchemy import select
from models.indicator import Indicator

def get_indicators(db):

    consulta = select(Indicator)
    resultado = db.execute(consulta)
    indicadors = resultado.scalars().all()

    return indicadors