from fastapi import FastAPI
from routes.health import router

app = FastAPI()

app.include_router(router)
