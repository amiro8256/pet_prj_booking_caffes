import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import (
    Base,
    field_not_null_str,
    field_null_desc_str,
)

from .association_tables import bookings_dishes

if TYPE_CHECKING:
    from .booking import Booking
    from .cafe import Cafe


class Dish(Base):
    """Класс таблицы dishes."""

    __tablename__ = 'dishes'

    name: Mapped[field_not_null_str]
    description: Mapped[field_null_desc_str | None]
    photo: Mapped[uuid.UUID | None] = mapped_column(
        Uuid(as_uuid=True, native_uuid=True),
        nullable=True,
        unique=True,
    )
    price: Mapped[int]

    cafe_id: Mapped[int] = mapped_column(ForeignKey('cafes.id'))
    cafe: Mapped['Cafe'] = relationship(
        back_populates='dishes',
        lazy='selectin',
    )
    bookings: Mapped[list['Booking']] = relationship(
        secondary=bookings_dishes,
        back_populates='dishes',
        lazy='selectin',
    ) 
