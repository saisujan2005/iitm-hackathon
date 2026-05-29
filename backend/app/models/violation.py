from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Violation(Base):
    __tablename__ = "violations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)