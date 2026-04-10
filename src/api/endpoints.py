from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import Session
from schemas.auth import AuthData, AuthToken
from schemas.user import CreateUser
from crud.user import user_crud

router = APIRouter()


@router.post("/auth/login")
async def login(data: AuthData) -> AuthToken:
    """Эндпоинт для авторизации пользователя."""
    # Здесь логика проверки данных и генерации токена
    # проверить данные в базе данных и создать JWT токен
    return AuthToken(access_token="fake_token", token_type="bearer")


@router.post("/users")
async def user_create(user_data: CreateUser):
    """Эндпоинт для создания нового пользователя."""
    async with Session() as session:
        new_user = await user_crud.create(session, user_data)
        # использовать правильную схему ответа
        return new_user

