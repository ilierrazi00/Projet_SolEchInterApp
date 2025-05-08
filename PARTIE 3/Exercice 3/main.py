from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

class Personnage(BaseModel):
    nom: str
    score: int

@app.post("/webhook/personnage")
def recevoir_personnage(p: Personnage):
    if p.score >= 90:
        niveau = "expert"
    elif p.score >= 60:
        niveau = "intermédiaire"
    else:
        niveau = "débutant"

    personnage_avec_niveau = {
        "nom": p.nom,
        "score": p.score,
        "niveau": niveau
    }

    # Enregistrement dans webhook_log.json
    log_path = Path("webhook_log.json")
    try:
        if log_path.exists():
            with open(log_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = []

        data.append(personnage_avec_niveau)

        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    except Exception as e:
        return {"error": str(e)}

    return personnage_avec_niveau
