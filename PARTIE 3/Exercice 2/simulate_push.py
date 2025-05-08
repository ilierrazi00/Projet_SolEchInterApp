import requests
import time

url = "http://localhost:8000/webhook/personnage"
headers = {"Content-Type": "application/json"}
data = {
    "nom": "Sasuke",
    "score": 90
}

try:
    print("📤 Envoi du JSON à l’API FastAPI...")
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    print("✅ Réponse :", response.json())
except Exception as e:
    print("❌ Échec :", e)
