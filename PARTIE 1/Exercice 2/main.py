# Importation des modules nécessaires de FastAPI
from fastapi import FastAPI, Header, HTTPException

# Création de l'application FastAPI
app = FastAPI()

# Définition d'une liste statique de personnages fictifs (sera renvoyée par l'API)
personnages = [
    {"nom": "Harry Potter", "univers": "Harry Potter"},
    {"nom": "Luke Skywalker", "univers": "Star Wars"}
]

# Déclaration d'une constante contenant le token secret attendu
TOKEN_SECRET = "super_token_123"

# Définition d'un endpoint GET accessible via l'URL /personnages
@app.get("/personnages")
def get_personnages(token: str = Header(None)):
    """
    Endpoint sécurisé : l'utilisateur doit fournir un token valide
    dans le header de la requête pour obtenir la liste des personnages.
    """
    # Vérifie si le token transmis est bien celui attendu
    if token != TOKEN_SECRET:
        # Si le token est invalide ou manquant, retourne une erreur HTTP 401 (non autorisé)
        raise HTTPException(status_code=401, detail="Accès refusé : token invalide")
    
    # Si le token est valide, retourne la liste des personnages
    return personnages
