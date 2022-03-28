import logging

from fastapi import FastAPI

from app.api import teams
from app.db import init_db


def create_application() -> FastAPI:
    application = FastAPI(
        openapi_url="/teams/openapi.json",
        docs_url="/teams/docs")
    application.include_router(
        teams.router,
        tags=["teams"])
    return application


app = create_application()
log = logging.getLogger("uvicorn")


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
