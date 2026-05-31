import json

from google import genai

from app.config import GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def extract_challan_details(image_bytes):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {
                "text": """
You are an OCR assistant.

Read the traffic challan image.

Extract:

- Vehicle Number
- Violation Description
- Legal Section
- Date
- Fine Amount

Return ONLY JSON.

Example:

{
  "vehicle_number": "KA01AB1234",
  "violation": "Triple Riding",
  "section": "194C",
  "date": "2025-05-20",
  "fine_amount": "1000"
}

If a field is missing, return null.
"""
            },
            {
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": image_bytes
                }
            }
        ]
    )

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

    try:

        return json.loads(text)

    except Exception:

        return {
            "vehicle_number": None,
            "violation": None,
            "section": None,
            "date": None,
            "fine_amount": None
        }
    

def explain_violation(
    violation: str,
    section: str
):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are DriveLegal AI.

Explain this traffic violation in simple language.

Violation:
{violation}

Section:
{section}

Keep the explanation under 4 sentences.

Mention:
- What the violation means
- Why it is illegal
- Safety reason
"""
    )

    return response.text    