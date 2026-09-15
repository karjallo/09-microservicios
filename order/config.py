from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    INTERNAL_SERVICE_TOKEN: str = "default_token"
    DATABASE_URL: str = "sqlite:///./app.db"

settings = Settings()