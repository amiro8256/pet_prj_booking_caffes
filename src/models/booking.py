from datetime import date
from enum import IntEnum
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Date, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base
from core.constants import MAX_LEN_STR
from .association_tables import (
    bookings_timeslots,
    bookings_dishes,
    bookings_tabels,
)

if TYPE_CHECKING:
    from .cafe import Cafe
    from .dish import Dish
    from .table import Table
    from .timeslot import TimeSlot
    from .user import User


class BookingStatus(IntEnum):
    """Класс статусов бронирования."""

    Canceled = 0
    Booking = 1
    Active = 2


class Booking(Base):
    """Класс таблицы bookings."""

    __tablename__ = 'bookings'

    guest_number: Mapped[int] = mapped_column(nullable=False)
    # Проверить парамметры поля
    note: Mapped[str] = mapped_column(String(MAX_LEN_STR), nullable=True)
    # установить дефолтное значение
    booking_date: Mapped[date] = mapped_column(Date, nullable=False)
    # native_enum=False отключает "нативный" ENUM в БД и хранит Enum.values (int/str)
    status: Mapped['BookingStatus'] = mapped_column(
        Enum(BookingStatus, native_enum=False),
        nullable=False,
        default=BookingStatus.Booking,
    )
    cafe_id: Mapped[int] = mapped_column(ForeignKey('cafes.id'))
    cafe: Mapped['Cafe'] = relationship(
        back_populates='bookings',
        lazy='select',
    )
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(
        back_populates='bookings',
        lazy='select',
    )
    tables: Mapped[list['Table']] = relationship(
        secondary=bookings_tabels,
        back_populates='bookings',
        lazy='select',
    )
    timeslots: Mapped[list['TimeSlot']] = relationship(
        secondary=bookings_timeslots,
        back_populates='bookings',
        lazy='select',
    )
    dishes: Mapped[list['Dish']] = relationship(
        secondary=bookings_dishes,
        back_populates='bookings',
        lazy='select',
    )
