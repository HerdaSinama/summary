from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

class Config(BaseConfig):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5434
    DB_NAME: str = "summary_db"
    DB_USER: str = "postgres"
    DB_PASSWORD: str

    DATABASE_URL: str | None = None

    YANDEX_API_KEY: str = "<API-ключ>"
    YANDEX_FOLDER_ID: str = "<идентификатор_каталога>"
    YANDEX_MODEL: str = "aliceai-image-art-3.0"

    CELERY_BROKER_URL: str = "amqp://guest:guest@localhost:5672//"
    CELERY_RESULT_BACKEND: str = "rpc://"

    @property
    def sync_database_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL.replace("postgresql+asyncpg://", "postgresql+psycopg://")
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

@lru_cache
def get_config() -> Config:
    return Config()

config = get_config()