from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RouletteHistory(BaseModel):
    history: list[int]

@app.get("/health")
def health():
    # BUG INTENTIONNEL : renvoie DOWN au lieu de UP
    return {"status": "DOWN"}

@app.post("/predict")
def predict(data: RouletteHistory):
    last = data.history[-1] if data.history else 0
    return {
        "last_number_received": last,
        "suggestion": "PAIR" if last % 2 == 0 else "IMPAIR"
    }
