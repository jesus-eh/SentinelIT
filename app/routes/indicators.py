from fastapi import APIRouter, Depends
from models.indicator import IndicatorCreate
from models.indicator import Indicator
from database import get_db
from services.indicators_service import obtener_indicador,            obtener_indicadorID, insertar_indicadores

router = APIRouter()

# Endpoint Get
@router.get("/indicators")
def get_indicators(db = Depends(get_db)):
    lista = obtener_indicador(db) # llamamos al services
    return lista

# Endpoint Get + ID
@router.get("/indicators/{id}")
def get_indicatorsID(id: int,db = Depends(get_db)):
    lista = obtener_indicadorID(db, id) # llamamos al services
    return lista

# Endpoint Post
@router.post("/indicators")
def post_indicators(indicator: IndicatorCreate, db = Depends(get_db)):

    subida = insertar_indicadores(indicator, db)
    
    return "Indicators subido"


# Endpoint Delete
@router.delete("/indicators/{id}")
def del_indicators(id: int):
    return "Indicators eliminado"