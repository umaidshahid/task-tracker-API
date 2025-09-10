import os
from pydantic import BaseSettings


class Settings(BaseSettings):
DATABASE_URL: str
SECRET_KEY: str
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
REDIS_URL: str = "redis://localhost:6379/0"


class Config:
env_file = ".env"


settings = Settings()