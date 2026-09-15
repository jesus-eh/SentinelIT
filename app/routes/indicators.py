from fastapi import APIRouter, Depends
from models.indicator import IndicatorCreate
from models.indicator import Indicator
from database import get_db
from services.indicators_service import obtener_indicador
router = APIRouter()

# Endpoint Get
@router.get("/indicators")
def get_indicators(db = Depends(get_db)):
    lista = obtener_indicador(db)
    return lista

# Endpoint Get + ID
@router.get("/indicators/{id}")
def get_indicatorsID(id: int,db = Depends(get_db)):

    return

# Endpoint Post
@router.post("/indicators")
def post_indicators(indicator: IndicatorCreate):
    return "Indicators subido"


# Endpoint Delete
@router.delete("/indicators/{id}")
def del_indicators(id: int):
    return "Indicators eliminado"