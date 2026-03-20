from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db import Base
from .association_tables import cafe_actions

if TYPE_CHECKING:
    from .cafe import Cafe


class Action(Base):
    """Модель акций."""

    __tablename__ = 'actions'

    description: Mapped[str] = mapped_column(nullable=False)
    photo_id: Mapped[str | None]
    cafe: Mapped[list['Cafe']] = relationship(
        secondary=cafe_actions,
        back_populates='actions',
        lazy='selectin',
    )
