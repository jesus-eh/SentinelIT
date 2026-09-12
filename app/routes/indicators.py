from fastapi import APIRouter

router = APIRouter()

@router.get("/indicators")
def get_indicators():
    return "Hola desde la ruta"