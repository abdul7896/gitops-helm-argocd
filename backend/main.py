from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def read_root():
    env = os.getenv("DEPLOY_ENV", "development")
    return {"message": f"Hello from {env}!", "service": "backend"}