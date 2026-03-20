from datetime import datetime
from typing import Annotated

from sqlalchemy import Integer, DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from .config import settings
from .constants import MAX_LEN_STR


field_not_null_str = Annotated[str, mapped_column(
    String(MAX_LEN_STR), nullable=False
)]

field_null_desc_str = Annotated[str, mapped_column(
    String, nullable=True
)]


class Base(DeclarativeBase):
    """Базовый класс для всех моделей."""

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    active: Mapped[bool] = mapped_column(default=True, nullable=False)
    create_at: Mapped[datetime] = mapped_column(
        DateTime(),
        server_default=func.current_timestamp(),
    )
    update_at: Mapped[datetime] = mapped_column(
        DateTime(),
        server_default=func.current_timestamp(),  # Исправить с сервер-дефолт на пайтон-дефолт
        server_onupdate=func.current_timestamp(),  # Исправить с сервер-дефолт на пайтон-дефолт
    )


sqlite_engine = create_engine(settings.DB_SQLite_URL, echo=True)
Session = sessionmaker(sqlite_engine)


def get_sync_session():
    """Синхронный генератор сессий."""
    with Session() as session:
        yield session


engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    """Асинхронный генератор сессий."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
