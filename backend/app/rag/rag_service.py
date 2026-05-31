from google import genai

from app.config import GEMINI_API_KEY
from app.rag.retriever import retrieve_context

import re

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def answer_with_rag(
    question: str
):

    # Detect section references
    section_match = re.search(
        r"section\s+(\d+[A-Z]?)",
        question,
        re.IGNORECASE
    )

    requested_section = None

    if section_match:

        requested_section = (
            section_match.group(1)
        )

    context = retrieve_context(
        question
    )

    prompt = f"""
You are DriveLegal AI.

You are a legal assistant for Indian traffic laws.

Use ONLY the legal context provided below.

Rules:

1. Do not invent facts.
2. Explain in simple language.
3. Mention the legal section whenever possible.
4. If the answer is not available in the context, say so clearly.
5. Give a short explanation.
6. End every answer with a Source section.

Requested Section:
{requested_section}

Legal Context:

{context}

User Question:

{question}

Answer Format:

Answer:
<your answer>

Explanation:
<simple explanation>

Source:
Motor Vehicles Act, 1988
<Section Number if available>
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text