from fastapi import APIRouter
from app.db.database import SessionLocal
from app.models.penalty import Penalty

router = APIRouter()


@router.get("/test/all")
def test_all():

    db = SessionLocal()

    rows = db.query(Penalty).all()

    return [
        {
            "id": row.id,
            "state": row.state,
            "violation": row.violation
        }
        for row in rows[:10]
    ]
