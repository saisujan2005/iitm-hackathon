from app.db.database import SessionLocal
from app.models.penalty import Penalty


def calculate_fine(data):

    db = SessionLocal()

    try:

        penalty = (
            db.query(Penalty)
            .filter(
                Penalty.state == data.state,
                Penalty.violation.ilike(
                    f"%{data.violation}%"
                )
            )
            .first()
        )

        if not penalty:

            return {
                "error": (
                    f"No violation found for "
                    f"'{data.violation}'"
                )
            }

        fine_amount = penalty.fine_amount

        return {
            "state": penalty.state,
            "violation": penalty.violation,
            "section": penalty.section,
            "fine_amount": fine_amount,
            "source_url": penalty.source_url
        }

    finally:
        db.close()