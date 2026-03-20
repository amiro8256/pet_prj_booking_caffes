from enum import IntEnum
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db import Base, field_not_null_str
from core.constants import MAX_LEN_STR, MAX_LEN_PHONE

from .association_tables import cafe_managers

if TYPE_CHECKING:
    from .booking import Booking
    from .cafe import Cafe


class UserRole(IntEnum):
    """Класс статуса юзера."""

    USER = 0
    MANAGER = 1
    ADMIN = 2


class User(Base):
    """
    Класс таблицы users.

    Ограничения: email или phone не должен быть пустым;
    комбинации username + email и name + phone уникальны.
    """
    __tablename__ = 'users'
    __table_args__ = (
        CheckConstraint(
            '(email IS NOT NULL) OR (phone IS NOT NULL)',
            name='user_contact_required',
        ),
        UniqueConstraint('username', 'email', name='unique_name_user_email'),
        UniqueConstraint('username', 'phone', name='unique_name_user_phone'),
    )

    username: Mapped[field_not_null_str]
    email: Mapped[str] = mapped_column(
        String(MAX_LEN_STR),
        nullable=True,
        index=True,
        unique=True,
    )
    phone: Mapped[str] = mapped_column(
        String(MAX_LEN_PHONE),
        nullable=True,
        index=True,
        unique=True,
    )
    tg_id: Mapped[str] = mapped_column(String(MAX_LEN_STR), unique=True)
    password_hash: Mapped[field_not_null_str]
    role: Mapped[int] = mapped_column(
        nullable=False,
        default=int(UserRole.USER),
    )
    cafes_manager: Mapped[list['Cafe']] = relationship(
        secondary=cafe_managers,
        back_populates='managers',
        lazy='selectin',
    )
    bookings: Mapped[list['Booking']] = relationship(
        back_populates='user',
        lazy='select',
    )

    # @validates('email', 'phone')
    # def validate_contact(self, key, value):
    #     """Проверяет, что указанно одно из двух полей."""
    #     if self.email is None and self.phone is None:
    #         raise ValueError("Должен быть указан email или phone")
    #     return value

