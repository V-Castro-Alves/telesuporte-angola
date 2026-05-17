from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    GOOGLE_API_KEY: str = ""
    MODEL_NAME: str = "gemini-1.5-flash"
    WHISPER_MODEL: str = "base"
    CHROMA_DB_PATH: str = "./data/chroma_db"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
