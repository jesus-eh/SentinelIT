from fastapi import APIRouter, Depends
from app.models.indicator import IndicatorCreate
from app.models.indicator import Indicator
from app.database import get_db
from app.services.indicators_service import indicators, indicatorsID, insert_indicadores, delete_indicador

router = APIRouter()

# Endpoint Get
@router.get("/indicators")
def get_indicators(db = Depends(get_db)):
    lista = indicators(db) # llamamos al services
    return lista

# Endpoint Get + ID
@router.get("/indicators/{id}")
def get_indicatorsID(id: int,db = Depends(get_db)):
    lista = indicatorsID(db, id) # llamamos al services
    return lista

# Endpoint Post
@router.post("/indicators")
def post_indicators(indicator: IndicatorCreate, db = Depends(get_db)):
    respuesta = insert_indicadores(indicator, db) # Llamamos al services
    return respuesta


# Endpoint Delete
@router.delete("/indicators/{id}")
def del_indicators(id: int, db = Depends(get_db)):
    respuesta = delete_indicador(id, db) # LLamamos al services
    return respuesta