import uuid
from typing import List, Union, TYPE_CHECKING

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, relationship, mapped_column

from core.constants import MAX_LEN_PHONE
from core.db import Base, field_not_null_str, field_null_desc_str

from .association_tables import cafe_actions, cafe_managers

if TYPE_CHECKING:
    from .action import Action
    from .booking import Booking
    from .dish import Dish
    from .table import Table
    from .timeslot import TimeSlot
    from .user import User


class Cafe(Base):
    """Класс таблицы cafes."""

    __tablename__ = 'cafes'

    name: Mapped[field_not_null_str]
    adress: Mapped[field_not_null_str]
    phone: Mapped[str] = mapped_column(String(MAX_LEN_PHONE), nullable=False)
    description: Mapped[Union[str, None]] = field_null_desc_str
    # as_uuid=определяет формат представления значения в Python-коде, str/uuid.UUID
    # =True вернёт объект uuid.UUID, =False вернёт строку, hex-формат, 32 символа без дефисов
    # native_uuid=определяет формат записи в бд; =True пытается использовать встроенный в бд тип uuid,
    # =False использует hex-строку или VARCHAR(32).
    photo: Mapped[Union[uuid.UUID, None]] = mapped_column(
        Uuid(as_uuid=True, native_uuid=True),
        nullable=True,
        unique=True,
    )
    managers: Mapped[list['User']] = relationship(
        secondary=cafe_managers,
        back_populates='cafes_manager',
        lazy='select',
    )
    actions: Mapped[List['Action']] = relationship(
        secondary=cafe_actions,
        back_populates='cafes',
        lazy='select',
    )
    bookings: Mapped[List['Booking']] = relationship(
        back_populates='cafe',
        lazy='select',
    )
    tables: Mapped[list['Table']] = relationship(
        back_populates='cafe',
        lazy='select',
    )
    time_slots: Mapped[list['TimeSlot']] = relationship(
        back_populates='cafe',
        lazy='select',
    )
    dishes: Mapped[list['Dish']] = relationship(
        back_populates='cafe',
        lazy='select',
    )
