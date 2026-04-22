from fastapi import FastAPI

from core.config import settings
from api.endpoints.user import router



app = FastAPI()

app.include_router(router)
