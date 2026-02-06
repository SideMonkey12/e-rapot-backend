from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """
    Application configuration settings loaded from environment variables.
    """
    APP_NAME: str
    APP_ENV: str = "development"
    APP_PORT: int = 8000

    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD:str

    class Config:
        """
        Configuration for Pydantic BaseSettings to specify the environment file.
        """
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()