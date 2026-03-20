from datetime import datetime

from pydantic import BaseModel

from models.cafe import Cafe


class ActionCreate(BaseModel):
    """Класс создания акции."""
    cafe_id: list[int]
    description: str
    photo_id: str | None


class ActionInfo(BaseModel):
    """Класс информации об акции."""
    id: int
    cafes: list['Cafe']
    description: str
    photo_id: str | None
    is_active: bool
    create_at: datetime
    updated_at: datetime


class ActionUpdate(BaseModel):
    """Класс обновления акции."""
    cafes_id: list[int] | None
    description: str | None
    photo_id: str | None
    is_active: bool | None
