import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt):

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        if "429" in str(e):
            return """
AI service quota exceeded.

Basic Financial Advice:
• Save at least 20% of income
• Maintain emergency fund
• Reduce high-interest debts
• Invest according to risk tolerance
"""

        return f"Error: {str(e)}"
