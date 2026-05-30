from app.db.database import SessionLocal
from app.models.penalty import Penalty


def calculate_fine(data):

    db = SessionLocal()

    try:

        print("Searching for:", data.violation)

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

        print("Found:", penalty)

        if not penalty:

            return {
                "error": (
                    f"No violation found for "
                    f"'{data.violation}'"
                )
            }

        return {
            "state": penalty.state,
            "violation": penalty.violation,
            "section": penalty.section,
            "fine_amount": penalty.fine_amount,
            "source_url": penalty.source_url
        }

    finally:
        db.close()