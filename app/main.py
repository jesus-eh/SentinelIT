from fastapi import FastAPI
from app.routes.health import router as health
from app.routes.indicators import router as indicators

app = FastAPI()

app.include_router(health)
app.include_router(indicators)
