from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_ai(question: str):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a traffic law assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content