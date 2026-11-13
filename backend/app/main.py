from fastapi import FastAPI
from app.api.routes import health

app = FastAPI(
    title="DocuMind AI API",
    version="1.0",
)


app.include_router(health.router)


@app.get("/")
def home():
    return {
        "message": "DocuMind AI API running On 8000",
    }
