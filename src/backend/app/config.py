"""Configuration settings for the application."""
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "SF Muni Predictor"
    VERSION: str = "1.0.0"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    REDIS_MAX_CONNECTIONS: int = 50
    
    # 511 API
    API_511_KEY: str = ""
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
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()