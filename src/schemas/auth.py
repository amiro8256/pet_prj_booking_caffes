from pydantic import BaseModel


class AuthData(BaseModel):
    """Схема для получения данных авторизации."""
    username: str
    password: str


class AuthToken(BaseModel):
    """Схема для возврата токена."""
    access_token: str
    token_type: str
