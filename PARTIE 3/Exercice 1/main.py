from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Personnage(BaseModel):
    nom: str
    score: int

@app.post("/webhook/personnage")
def recevoir_personnage(p: Personnage):
    if p.score >= 90:
        niveau = "expert"
    elif p.score >= 70:
        niveau = "intermédiaire"
    else:
        niveau = "débutant"
    
    return {
        "nom": p.nom,
        "score": p.score,
        "niveau": niveau
    }
