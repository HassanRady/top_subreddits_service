from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    REDDIT_CLIENT_ID: str
    REDDIT_CLIENT_SECRET: str
    REDDIT_USER_AGENT: str


@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()