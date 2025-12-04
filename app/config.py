import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local.db")
    APP_ENV = os.getenv("APP_ENV", "development")
    AI_PROVIDER = os.getenv("AI_PROVIDER", "none")
    AI_API_KEY = os.getenv("AI_API_KEY", "")

settings = Settings()
