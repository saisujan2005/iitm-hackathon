from app.db.database import SessionLocal
from app.models.penalty import Penalty


def save_penalties(records):

    db = SessionLocal()

    try:

        # Remove old Karnataka records
        db.query(Penalty).filter(
            Penalty.state == "Karnataka"
        ).delete()

        db.commit()

        for record in records:

            penalty = Penalty(
                state=record["state"],
                violation=record["violation"],
                section=record["section"],
                fine_amount=record["fine_amount"],
                source_url=(
                    "https://vijayanagarapolice.karnataka.gov.in/"
                    "storage/pdf-files/traffic%20rules%20%20and%20fines%20e.pdf"
                )
            )

            db.add(penalty)

        db.commit()

        print(
            f"Saved {len(records)} penalties"
        )

    finally:
        db.close()