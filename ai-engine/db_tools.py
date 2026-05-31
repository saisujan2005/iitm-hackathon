from app.db.database import SessionLocal
from app.models.penalty import Penalty


def find_violation(state: str, violation: str):

    db = SessionLocal()

    try:

        result = (
            db.query(Penalty)
            .filter(
                Penalty.state == state,
                Penalty.violation.ilike(
                    f"%{violation}%"
                )
            )
            .first()
        )

        if not result:
            return None

        return {
            "state": result.state,
            "violation": result.violation,
            "section": result.section,
            "fine_amount": result.fine_amount,
            "source_url": result.source_url
        }

    finally:
        db.close()