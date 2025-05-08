from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Variable globale pour activer/désactiver les notifications
notifications_active = True

# Modèle du personnage
class Personnage(BaseModel):
    nom: str
    score: int

@app.post("/webhook/personnage")
def recevoir_personnage(personnage: Personnage):
    # Déterminer le niveau
    niveau = "débutant"
    if personnage.score >= 90:
        niveau = "expert"
    elif personnage.score >= 50:
        niveau = "intermédiaire"

    donnees = personnage.dict()
    donnees["niveau"] = niveau

    # ✅ Affichage console
    print(f"✅ Personnage ajouté avec succès : {donnees['nom']} (niveau : {niveau})")

    # ✅ Si notifications activées, écrire dans notifications.txt
    if notifications_active:
        try:
            with open("notifications.txt", "a", encoding="utf-8") as f:
                f.write(json.dumps(donnees, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"⚠️ Erreur lors de l'écriture du fichier : {e}")
    else:
        print("🔕 Notifications désactivées.")

    return donnees

# ✅ Activer les notifications
@app.post("/subscribe")
def subscribe():
    global notifications_active
    notifications_active = True
    return {"message": "✅ Notifications activées"}

# ✅ Désactiver les notifications
@app.post("/unsubscribe")
def unsubscribe():
    global notifications_active
    notifications_active = False
    return {"message": "🚫 Notifications désactivées"}
