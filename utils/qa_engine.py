import os
from dotenv import load_dotenv
from openai import OpenAI  # replace with Gemini API client if different

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini API client
gemini = OpenAI(api_key=api_key)

def ask_question(question, context):
    """
    Sends a question and context to Gemini API and returns the answer.
    """
    prompt = f"Answer the question based on the following text:\n\n{context}\n\nQuestion: {question}"
    response = gemini.chat.create(
        model="gemini-1.5",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
