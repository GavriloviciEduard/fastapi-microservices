import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger("uvicorn")


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["models.team"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
