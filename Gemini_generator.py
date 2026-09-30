import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_answer(question):

    prompt = f"""
    You are EduGenie, an AI learning assistant.

    Student Question:
    {question}

    Give a simple, clear and educational answer.
    Explain step by step when necessary.
    """

    response = model.generate_content(prompt)

    return response.text
