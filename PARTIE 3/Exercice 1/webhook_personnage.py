from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modèle attendu pour le POST
class Personnage(BaseModel):
    nom: str
    score: int

# Route webhook
@app.post("/webhook/personnage")
async def recevoir_personnage(p: Personnage):
    # Déterminer le niveau selon le score
    if p.score >= 90:
        niveau = "expert"
    elif p.score >= 70:
        niveau = "intermédiaire"
    else:
        niveau = "débutant"

    # Afficher dans la console
    print(f"👤 Personnage reçu : {p.nom} - Score : {p.score} - Niveau : {niveau}")

    # Réponse enrichie
    return {
        "nom": p.nom,
        "score": p.score,
        "niveau": niveau
    }
