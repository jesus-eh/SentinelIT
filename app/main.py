from fastapi import FastAPI
from routes.health import router as health
from routes.health import router as indicators

app = FastAPI()

app.include_router(health)
app.include_router(indicators)
