from fastapi import FastAPI

from core.config import settings
from api.endpoints import router



app = FastAPI()

app.include_router(router)
