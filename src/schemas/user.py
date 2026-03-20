from pydantic import BaseModel


class CreateUser(BaseModel):
    """Модель для создания нового пользователя."""
    username: str
    email: str | None
    phone: str | None
    tg_id: str | None
    password: str


class UserInfo(BaseModel):
    """Модель для получения информации о пользователе."""
    id: int
# повторяющийся блок
    username: str
    email: str | None
    phone: str | None
    tg_id: str | None

    role: int
    active: bool
    create_at: str
    update_at: str


class UserShortInfo(BaseModel):
    """Модель для получения краткой информации о пользователе."""
    id: int
# повторяющийся блок
    username: str
    email: str | None
    phone: str | None
    tg_id: str | None


class UserUpdate(BaseModel):
    """Модель для обновления информации о пользователе."""
    username: str | None
    email: str | None
    phone: str | None
    tg_id: str | None
    role: int | None
    password: str | None