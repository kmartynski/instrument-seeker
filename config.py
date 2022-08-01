from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    email_address: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
