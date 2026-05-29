from app.db.database import Base, engine

# Import ALL models here
from app.models.penalty import Penalty
from app.models.source import Source

Base.metadata.create_all(bind=engine)

print("Tables created successfully")