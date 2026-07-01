import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Enterprise Pattern: Centralized Configuration Management
    Uses Pydantic BaseSettings to validate and cast environment variables.
    """
    model_name: str = "gemini-2.5-flash"
    google_genai_use_vertexai: str = "0"
    app_name: str = "production_api_app"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        # Allows extra env variables like GOOGLE_API_KEY without failing
        extra = "ignore"

def get_settings() -> Settings:
    """Dependency provider for FastAPI."""
    return Settings()
