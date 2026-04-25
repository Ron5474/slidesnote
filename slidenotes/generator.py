import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("API_KEY", "test"),
    base_url=os.environ.get("BASE_URL", "https://aiapi.paid.lol"),
)

SYSTEM_PROMPT = """You are a note-taking assistant for a graduate AI student.
Given the following lecture slides, generate comprehensive, structured markdown notes with:
- A title and lecture overview
- Key concepts with clear explanations
- Important formulas or definitions (in code blocks)
- Summary bullets at the end"""


def generate(slide_text: str) -> str:
    """Send extracted slide text to the LLM and return structured markdown notes."""
    response = client.chat.completions.create(
        model="main",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": slide_text},
        ],
    )
    return response.choices[0].message.content
