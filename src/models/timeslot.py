from datetime import time
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base
from .association_tables import bookings_timeslots

if TYPE_CHECKING:
    from .cafe import Cafe
    from .booking import Booking


class TimeSlot(Base):
    """Класс таблицы time_slots."""

    __tablename__ = 'time_slots'

    cafe_id: Mapped[int] = mapped_column(ForeignKey('cafes.id'))
    cafe: Mapped['Cafe'] = relationship(
        back_populates='time_slots',
        lazy='select',
    )
    start_time: Mapped[time] = mapped_column(Time, nullable=False)
    end_time: Mapped[time] = mapped_column(Time, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    booking: Mapped[list['Booking']] = relationship(
        secondary=bookings_timeslots,
        back_populates='time_slots',
        lazy='select',
    )
