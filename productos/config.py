from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    INTERNAL_SERVICE_TOKEN: str
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRE_MINUTES: int


    class Config:
        env_file = "../.env"

settings = Settings()
