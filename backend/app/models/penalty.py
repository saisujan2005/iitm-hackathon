from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Penalty(Base):
    __tablename__ = "penalties"

    id = Column(Integer, primary_key=True, index=True)
    state = Column(String)
    violation = Column(String)
    fine_amount = Column(Integer)