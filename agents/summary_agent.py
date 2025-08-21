import os
from groq import Groq

class SummaryAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("Set GROQ_API_KEY in .env")
        self.client = Groq(api_key=api_key)

    def run(self, insights):
        prompt = f"Summarize the following insights in 3-5 sentences for a manager:\n{insights}"
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful manager assistant."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile"
        )
        return response.choices[0].message.content
