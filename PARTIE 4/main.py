from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Personnage(BaseModel):
    nom: str
    score: int

@app.post("/traitement")
def traitement(personnage: Personnage):
    niveau = "débutant"
    if personnage.score >= 90:
        niveau = "expert"
    elif personnage.score >= 50:
        niveau = "intermédiaire"

    return {
        "nom": personnage.nom,
        "score": personnage.score,
        "niveau": niveau
    }
