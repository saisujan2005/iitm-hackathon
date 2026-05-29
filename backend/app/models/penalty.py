from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.db.database import Base


class Penalty(Base):

    __tablename__ = "penalties"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    state = Column(
        String,
        nullable=False
    )

    violation = Column(
        String,
        nullable=False
    )

    section = Column(
        String,
        nullable=True
    )

    fine_amount = Column(
        String,
        nullable=False
    )

    source_url = Column(
        String,
        nullable=True
    )

    last_updated = Column(
        DateTime,
        default=datetime.utcnow
    )