from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CrudBase:
    """Базовый класс CRUD операций."""

    def __init__(self, model):
        self.model = model

    async def get(self, obj_id: int, session: AsyncSession):
        """Получение объекта из бд по его id."""
        stmt = select(self.model).where(self.model.id == obj_id)
        res = await session.execute(stmt)
        return res.first()
