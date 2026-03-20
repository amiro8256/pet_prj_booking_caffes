from fastapi import APIRouter

from core.db import AsyncSessionLocal


router = APIRouter()


@router.post("/auth/login")
async def login():