from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Table,
)

from core.db import Base
from core.constants import QUANTITY_DISHES


cafe_actions = Table(
    'cafe_actions',
    Base.metadata,
    Column('cafe_id', ForeignKey('cafes.id'), primary_key=True),
    Column('action_id', ForeignKey('actions.id'), primary_key=True),
)

cafe_managers = Table(
    'cafe_managers',
    Base.metadata,
    Column('cafe_id', ForeignKey('cafes.id'), primary_key=True),
    Column('manager_id', ForeignKey('users.id'), primary_key=True),
)

bookings_tabels = Table(
    'bookings_tabels',
    Base.metadata,
    Column('booking_id', ForeignKey('bookings.id'), primary_key=True),
    Column('table_id', ForeignKey('tables.id'), primary_key=True),
)

bookings_timeslots = Table(
    'bookings_timeslots',
    Base.metadata,
    Column('booking_id', ForeignKey('bookings.id'), primary_key=True),
    Column('time_slots_id', ForeignKey('time_slots.id'), primary_key=True),
)

bookings_dishes = Table(
    'bookings_dishes',
    Base.metadata,
    Column('booking_id', ForeignKey('bookings.id'), primary_key=True),
    Column('dish_id', ForeignKey('dishes.id'), primary_key=True),
    Column('quantity', Integer, nullable=False, default=QUANTITY_DISHES)
)
