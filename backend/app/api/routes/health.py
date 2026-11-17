from fastapi import APIRouter
from app.core.config import settings

version = settings.APP_VERSION
env = settings.ENVIRONMENT

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "documind-api",
        "version": version,
        "environment": env,
    }
