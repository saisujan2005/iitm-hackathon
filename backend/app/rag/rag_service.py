from google import genai

from app.config import GEMINI_API_KEY
from app.rag.retriever import retrieve_context

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def answer_with_rag(
    question: str
):

    context = retrieve_context(
        question
    )

    prompt = f"""
You are DriveLegal AI.

Use the legal context provided below.

Explain the answer in simple language.

Mention the relevant section if available.

Do not invent facts outside the context.

Context:

{context}

Question:

{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text