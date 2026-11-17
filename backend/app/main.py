from fastapi import FastAPI
from app.api.routes import health
from app.core.config import settings

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
        "message": f"Welcome to {title} at 8000",
    }
