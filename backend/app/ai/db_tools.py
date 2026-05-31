from app.db.database import SessionLocal
from app.models.penalty import Penalty


def search_violation(question: str):

    db = SessionLocal()

    try:

        violations = db.query(
            Penalty
        ).all()

        question = question.lower()

        for violation in violations:

            violation_name = (
                violation.violation.lower()
            )

            if violation_name in question:
                return violation

        return None

    finally:
        db.close()


def search_violation_by_state(
    state: str,
    violation: str
):

    db = SessionLocal()

    try:

        result = (
            db.query(Penalty)
            .filter(
                Penalty.state.ilike(
                    f"%{state}%"
                ),
                Penalty.violation.ilike(
                    f"%{violation}%"
                )
            )
            .first()
        )

        return result

    finally:
        db.close()


def get_all_states():

    db = SessionLocal()

    try:

        states = (
            db.query(Penalty.state)
            .distinct()
            .all()
        )

        return [
            state[0]
            for state in states
        ]

    finally:
        db.close()


def get_violations_by_state(
    state: str
):

    db = SessionLocal()

    try:

        violations = (
            db.query(Penalty)
            .filter(
                Penalty.state == state
            )
            .all()
        )

        return violations

    finally:
        db.close()



def search_by_section(section: str):

    db = SessionLocal()

    try:

        penalties = db.query(
            Penalty
        ).all()

        for penalty in penalties:

            if not penalty.section:
                continue

            if section.lower() in penalty.section.lower():

                return penalty

        return None

    finally:
        db.close()        