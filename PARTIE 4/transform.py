import json
import requests

FICHIER = "notifications.txt"
URL = "http://127.0.0.1:8000/traitement"

with open(FICHIER, "r", encoding="utf-8") as f:
    for ligne in f:
        try:
            perso = json.loads(ligne)
            perso["score"] *= 2  # Ajoute le score doublé
            response = requests.post(URL, json=perso)
            print("📥 Reçu :", response.json())
        except Exception as e:
            print("❌ Erreur sur :", ligne.strip())
            print(e)
