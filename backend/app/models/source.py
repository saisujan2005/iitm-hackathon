from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.database import Base


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)

    # Karnataka, Delhi, etc.
    state = Column(String, nullable=False)

    # Official PDF / website URL
    url = Column(String, nullable=False, unique=True)

    # SHA256 hash of latest downloaded content
    last_hash = Column(String, nullable=True)

    # Last time source was checked
    last_checked = Column(DateTime, default=datetime.utcnow)

    # Last time source changed
    last_updated = Column(DateTime, default=datetime.utcnow)

    # PDF, Website, API
    source_type = Column(String, default="PDF")

    def __repr__(self):
        return (
            f"<Source(state='{self.state}', "
            f"source_type='{self.source_type}')>"
        )