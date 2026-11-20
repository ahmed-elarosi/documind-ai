from fastapi import APIRouter
from app.core.config import settings

version = settings.APP_VERSION
env = settings.ENVIRONMENT
title = settings.APP_NAME


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": title,
        "version": version,
        "environment": env,
    }
