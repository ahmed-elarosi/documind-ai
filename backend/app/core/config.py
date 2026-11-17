from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    APP_NAME: str = "DocuMind AI API"
    APP_VERSION: str = "0.1.0"

    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    LOG_LEVEL: str = "DEBUG"
