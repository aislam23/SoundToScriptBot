from pydantic_settings import BaseSettings
from pydantic import SecretStr

class Settings(BaseSettings):
    # Telegram Bot settings
    BOT_TOKEN: SecretStr
    CHANNEL_USERNAME: str = "@baldfrombrowser"
    
    # Database settings
    DATABASE_URL: str = "sqlite+aiosqlite:///bot_database.db"
    
    # Redis settings (для будущего масштабирования)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Rate limiting
    RATE_LIMIT: int = 1  # seconds
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Создаем глобальный экземпляр настроек
settings = Settings() 