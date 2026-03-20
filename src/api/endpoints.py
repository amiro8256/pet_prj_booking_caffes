from fastapi import APIRouter
from sqlalchemy.sql import text

from core.db import AsyncSessionLocal


router = APIRouter()


@router.get('/')
async def hellow():
    async with AsyncSessionLocal() as session:
        try:
            await session.execute(text('SELECT 1'))
            return {'hellow': 'Привет мир'}
        except Exception as e:
            return {'error': f"Failed to connect to PostgreSQL: {str(e)}"}