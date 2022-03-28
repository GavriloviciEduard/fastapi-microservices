import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    database_url: AnyUrl = os.getenv("DATABASE_URL")
    team_service_url: AnyUrl = os.getenv("TEAM_SERVICE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
