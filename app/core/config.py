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

    YANDEX_API_KEY: str
    YANDEX_FOLDER_ID: str
    YANDEX_MODEL: str = "aliceai-image-art-3.0"

    CELERY_BROKER_URL: str = "amqp://guest:guest@localhost:5672//"
    CELERY_RESULT_BACKEND: str = "rpc://"
    CELERY_DB_HOST: str = "db"
    CELERY_DB_PORT: int = 5432

    S3_ENDPOINT_URL: str = "http://s3:9000" 
    S3_BACE_URL: str = "http://localhost:9000"
    S3_ACCESS_KEY_ID: str = "minioadmin"
    S3_SECRET_ACCESS_KEY: str = "minioadmin"
    S3_REGION_NAME: str = "us-east-1"
    S3_BUCKET_NAME: str = "dev-bucket"

    @property
    def sync_database_url(self) -> str:
        """if self.DATABASE_URL:
            return self.DATABASE_URL.replace("postgresql+asyncpg://", "postgresql+psycopg://")"""
        
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.CELERY_DB_HOST}:{self.CELERY_DB_PORT}/{self.DB_NAME}"

@lru_cache
def get_config() -> Config:
    return Config()

config = get_config()