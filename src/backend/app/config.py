"""Configuration settings for the application."""
from functools import lru_cache
from pathlib import Path
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # API
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "GoTime"
    VERSION: str = "1.0.0"
    
    # Redis
    REDIS_URL: str = Field(default="")
    REDIS_MAX_CONNECTIONS: int = 50
    
    # 511 API
    API_511_KEY: str = Field(
        default="",
        description="511 API key for accessing transit data. Required for API access."
    )
    API_511_BASE_URL: str = "http://api.511.org/transit"


    # Polling
    POLL_INTERVAL_SECONDS: int = 30
    
    # CORS
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "https://yourdomain.vercel.app"
    ]
    
    # Prediction defaults
    DEFAULT_WALKING_SPEED_MPS: float = 1.4
    DEFAULT_BUFFER_MINUTES: float = 2.0
    
    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        # Looks for .env file in the backend directory (parent of app/)
    )
    
    @field_validator("API_511_KEY")
    @classmethod
    def validate_api_key(cls, v: str) -> str:
        """Validate that API key is provided (non-empty)."""
        if not v or not v.strip():
            raise ValueError(
                "API_511_KEY is required. Please set it in your .env file or environment variables. "
                "See .env.example for reference."
            )
        return v.strip()


@lru_cache()
def get_settings() -> Settings:
    return Settings()