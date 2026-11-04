from fastapi import FastAPI

app = FastAPI(title="DocuMind AI API", version="1.0")


@app.get("/")
def home():
    return {"message": "DocuMind AI API running"}
