from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import Session
from schemas.user import CreateUser
from crud.user import user_crud

router = APIRouter()


@router.post("/users")
async def user_create(user_data: CreateUser):
    """Создает нового пользователя с указанными данными."""
    async with Session() as session:
        new_user = await user_crud.create(session, user_data)
        # использовать правильную схему ответа
        return new_user


@router.get("/users")
async def get_all_users():
    """
    Возвращает информацию о всех пользователях.

    Только для администраторов или менеджеров.
    """
    pass


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    """
    Возвращает информацию о пользователе по его ID.

    Только для администраторов или менеджеров.
    """
    pass


@router.patch("/users/{user_id}")
async def update_user(user_id: int):
    """
    Обновление информации о пользователе.

    Только для администраторов или менеджеров.
    """

