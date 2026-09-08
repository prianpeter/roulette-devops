from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RouletteHistory(BaseModel):
    history: list[int]

@app.get("/health")
def health():
    return {"status": "UP"}

@app.post("/predict")
def predict(data: RouletteHistory):
    last = data.history[-1] if data.history else 0
    return {
        "last_number_received": last,
        "suggestion": "PAIR" if last % 2 == 0 else "IMPAIR"
    }
