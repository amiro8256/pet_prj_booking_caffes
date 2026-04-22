from fastapi import APIRouter

from schemas.auth import AuthData, AuthToken

router = APIRouter()


@router.post("/auth/login")
async def login(data: AuthData) -> AuthToken:
    """Эндпоинт для авторизации пользователя."""
    # Здесь логика проверки данных и генерации токена
    # проверить данные в базе данных и создать JWT токен
    return AuthToken(access_token="fake_token", token_type="bearer")