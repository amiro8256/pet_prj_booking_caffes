from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base
from .association_tables import bookings_tables

if TYPE_CHECKING:
    from .booking import Booking
    from .cafe import Cafe


class Table(Base):
    """Класс таблицы tables."""

    __tablename__ = 'tables'
    seats_number: Mapped[int]
    description: Mapped[str]
    cafe_id: Mapped[int] = mapped_column(ForeignKey('cafes.id'))
    cafe: Mapped['Cafe'] = relationship(
        back_populates='tables',
        lazy='select',
    )
    bookings: Mapped[list['Booking']] = relationship(
        secondary=bookings_tables,
        back_populates='tables',
        lazy='select',
    )
