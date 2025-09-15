
from pydantic import ValidationError
from schema import ResumeData
from openai import OpenAI
import httpx
from constant import *
import docx2txt
import fitz

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text("text")
    return text


def extract_text_from_docx(file) -> str:
    return docx2txt.process(file)

async def extract_with_ai(text: str) -> ResumeData:
    prompt = f"""
    You are a resume parser. Extract structured details from this resume and return JSON
    that matches the schema:
    {ResumeData.model_json_schema()}

    Resume Text:
    {text[:4000]}
    """

    raw_json = {}

    if USE_PROVIDER == "openai":
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"}
        )
        raw_json = response.choices[0].message.content

    elif USE_PROVIDER == "groq":
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
                json={
                    "model": "llama-3.1-70b-versatile",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0,
                    "response_format": {"type": "json_object"}
                },
            )
            raw_json = response.json()["choices"][0]["message"]["content"]

    # Validate with Pydantic
    try:
        data = ResumeData.model_validate_json(raw_json)
        return data
    except ValidationError as e:
        raise ValueError(f"Validation failed: {e}")
