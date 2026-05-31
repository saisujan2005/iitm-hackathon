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
Extract the traffic violation and state.

Return ONLY valid JSON.

Example:

{{
    "state": "Delhi",
    "violation": "Triple Riding"
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

    intent = extract_intent(
        question
    )

    state = intent.get(
        "state",
        ""
    )

    violation = intent.get(
        "violation",
        ""
    )

    print("QUESTION:", question)
    print("STATE:", state)
    print("VIOLATION:", violation)

    # State-aware search

    if state and violation:

        penalty = (
            search_violation_by_state(
                state,
                violation
            )
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

    # Fallback search

    penalty = search_violation(
        question
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

       # RAG Fallback

    return answer_with_rag(question)