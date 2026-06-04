import json

from google import genai

from app.rag.rag_service import answer_with_rag
from app.config import GEMINI_API_KEY

from app.ai.db_tools import (
    search_violation,
    search_violation_by_state
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def extract_intent(question: str):

    prompt = f"""
Extract the traffic violation and state from the question.

Return ONLY valid JSON.

Examples:

Question: helmet fine in punjab

{{
    "state": "Punjab",
    "violation": "Helmet"
}}

Question: triple riding fine in telangana

{{
    "state": "Telangana",
    "violation": "Triple Riding"
}}

Question: what is the minimum age for driving

{{
    "state": "",
    "violation": ""
}}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    try:

        text = response.text.strip()

        if text.startswith("```json"):
            text = (
                text.replace(
                    "```json",
                    ""
                )
                .replace(
                    "```",
                    ""
                )
                .strip()
            )

        return json.loads(text)

    except Exception:

        return {
            "state": "",
            "violation": ""
        }


def answer(question: str):

    intent = extract_intent(question)

    state = intent.get(
        "state",
        ""
    )

    violation = intent.get(
        "violation",
        ""
    )

    print("=" * 50)
    print("QUESTION :", question)
    print("STATE    :", state)
    print("VIOLATION:", violation)
    print("=" * 50)

    # ---------------------------------
    # Violation synonym mapping
    # ---------------------------------

    violation_map = {
        "overspeeding": "speed",
        "over speed": "speed",
        "speeding": "speed",
        "helmet": "helmet",
        "triple riding": "triple",
        "seat belt": "seat",
        "insurance": "insurance",
        "pollution": "pollution",
        "license": "licence",
        "licence": "licence",
        "mobile phone": "mobile",
        "drunk driving": "drunk"
    }

    search_term = violation.lower()

    for key, value in violation_map.items():

        if key in search_term:

            search_term = value
            break

    # ---------------------------------
    # State-aware penalty lookup
    # ---------------------------------

    if state and search_term:

        penalty = search_violation_by_state(
            state,
            search_term
        )

        print(
            "STATE SEARCH RESULT:",
            penalty
        )

        if penalty:

            return (
                f"Violation: {penalty.violation}\n\n"
                f"State: {penalty.state}\n\n"
                f"Fine: ₹{penalty.fine_amount}\n\n"
                f"Section: {penalty.section}\n\n"
                f"Source:\n"
                f"{penalty.source_url}"
            )

    # ---------------------------------
    # General law questions
    # ---------------------------------

    general_questions = [
        "what is",
        "how to",
        "how do",
        "minimum age",
        "learner",
        "digilocker",
        "documents",
        "rc",
        "registration",
        "validity",
        "can i",
        "can a",
        "why",
        "when"
    ]

    if any(
        phrase in question.lower()
        for phrase in general_questions
    ):
        return answer_with_rag(
            question
        )

    # ---------------------------------
    # Generic penalty lookup
    # ---------------------------------

    penalty_keywords = [
        "fine",
        "penalty",
        "challan",
        "helmet",
        "triple riding",
        "overspeed",
        "speeding",
        "seat belt",
        "drunk driving",
        "mobile phone",
        "insurance",
        "pollution"
    ]

    if any(
        keyword in question.lower()
        for keyword in penalty_keywords
    ):

        penalty = search_violation(
            question
        )

        print(
            "GENERIC SEARCH RESULT:",
            penalty
        )

        if penalty:

            return (
                f"Violation: {penalty.violation}\n\n"
                f"State: {penalty.state}\n\n"
                f"Fine: ₹{penalty.fine_amount}\n\n"
                f"Section: {penalty.section}\n\n"
                f"Source:\n"
                f"{penalty.source_url}"
            )

    # ---------------------------------
    # Final fallback
    # ---------------------------------

    return answer_with_rag(
        question
    )