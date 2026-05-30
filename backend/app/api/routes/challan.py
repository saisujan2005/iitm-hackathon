from fastapi import APIRouter

from app.schemas.challan_schema import ChallanRequest
from app.services.challan_service import calculate_fine

from app.db.database import SessionLocal
from app.models.penalty import Penalty

router = APIRouter()


@router.post("/calculate")
def calculate_challan(data: ChallanRequest):
    return calculate_fine(data)


@router.get("/violations/{state}")
def get_violations(state: str):

    db = SessionLocal()

    try:

        violations = (
            db.query(Penalty)
            .filter(
                Penalty.state == state
            )
            .all()
        )

        return [
            {
                "id": item.id,
                "violation": item.violation,
                "section": item.section,
                "fine_amount": item.fine_amount,
            }
            for item in violations
        ]

    finally:
        db.close()