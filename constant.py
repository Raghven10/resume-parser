import os
from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

USE_PROVIDER = os.getenv("USE_PROVIDER", 'groq')
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@localhost:5432/resumedb")