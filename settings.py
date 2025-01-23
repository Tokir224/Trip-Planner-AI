import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PEXEL_API_KEY = os.getenv("PEXEL_API_KEY")
MODEL = "llama3-70b-8192"
