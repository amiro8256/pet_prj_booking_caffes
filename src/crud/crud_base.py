from typing import Optional, TypeVar, List

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import Base
from models.user import User, UserRole


class CrudBase:
    """Базовый класс CRUD операций."""

    ModelType = TypeVar('ModelType', bound=Base)
    CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
    UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)

    def __init__(self, model: type[ModelType]):
        """Сохраняят класс ORM. с которым работает CRUD."""
        self.model = model

    async def get(
            self,
            session: AsyncSession,
            obj_id: int
    ) -> Optional[ModelType]:
        """Получение объекта из бд по его id."""
        stmt = select(self.model).where(self.model.id == obj_id)
        res = await session.execute(stmt)
        return res.first()

    async def get_multi(
            self,
            session: AsyncSession,
            user: User,
            is_active=False
    ) -> List[ModelType]:
        """Получить все объекты."""
        if user.role in (
            UserRole.MANAGER, UserRole.ADMIN
        ) and is_active is False:
            stmt = select(self.model)
        else:
            stmt = select(self.model).where(self.model.active.is_(False))

        res = await session.execute(stmt)
        return res.scalars().all()

    async def create(
            self,
            session: AsyncSession,
            obj_in: CreateSchema,
    ) -> ModelType:
        """Создать новый объект из схемы "obj_in" и вернуть его."""
        new_obj = self.model(obj_in.model_dump())
        session.add(new_obj)
        await session.commit()
        await session.refresh(new_obj)
        return new_obj

    async def update(
            self,
            session: AsyncSession,
            obj_in: UpdateSchema,
            obj_id: int,
    ) -> ModelType:
        """Частично измененить объект из схемы "obj_in" и вернуть его."""
        obj_db = self.get(session, obj_id)
        if obj_db:
            obj_in_data = obj_in.model_dump(exclude_unset=True)
            for attr, val in obj_in_data.values():
                if hasattr(obj_db, attr):
                    setattr(obj_db, attr, val)
            session.add(obj_db)
            await session.commit()
            await session.refresh(obj_db)
            return obj_db
        # else:
            # Вернуть онибку, что объект не найден
