from app.db.database import SessionLocal
from app.models.penalty import Penalty

db = SessionLocal()

rows = db.query(Penalty).all()

print(f"Found {len(rows)} records\n")

for row in rows[:10]:

    print(
        row.violation,
        "|",
        row.fine_amount
    )

db.close()