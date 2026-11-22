import logging

from fastapi import FastAPI
from app.api.routes import health
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

title = settings.APP_NAME
version = settings.APP_VERSION
debug = settings.DEBUG


app = FastAPI(
    title=title,
    description="AI Powered Document Intelligence Platform",
    version=version,
    debug=debug,
)


app.include_router(health.router)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {title}",
    }
