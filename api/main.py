from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# 1. On initialise notre application (notre serveur)
app = FastAPI()

# 2. On définit la forme des données que l'utilisateur doit envoyer en POST
class DrawHistory(BaseModel):
    history: List[int]

# 3. La route GET : juste pour vérifier si l'application est allumée
@app.get("/health")
def healthcheck():
    return {"status": "UP"}

# 4. La route POST : reçoit les numéros et renvoie une prédiction
@app.post("/predict")
def predict_next(draw: DrawHistory):
    # On regarde le dernier numéro envoyé dans la liste
    last_number = draw.history[-1]
    
    # Règle simple : si le dernier numéro est pair, on suggère IMPAIR
    if last_number % 2 == 0:
        suggestion = "IMPAIR"
    else:
        suggestion = "PAIR"
        
    return {
        "last_number_received": last_number,
        "suggestion": suggestion
    }
