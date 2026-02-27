from fastapi import FastAPI

app = FastAPI(title="DevNarrate API")

@app.get("/health")
def health_check():
    return {"status": "ok"}