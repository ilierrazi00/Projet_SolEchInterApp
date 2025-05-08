# Importation des modules nécessaires depuis FastAPI
from fastapi import FastAPI, Header, HTTPException
# Importation du middleware CORS pour autoriser l'accès à l'API depuis d'autres origines
from fastapi.middleware.cors import CORSMiddleware

# Création de l'application FastAPI
app = FastAPI()

# Ajout du middleware CORS pour permettre les requêtes depuis des clients front-end (ex: HTML, React, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Autorise toutes les origines (*) — à limiter en production pour la sécurité
    allow_credentials=True,         # Autorise l'envoi de cookies et d'en-têtes d'authentification
    allow_methods=["*"],            # Autorise toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],            # Autorise tous les headers, y compris les headers personnalisés comme "token"
)

# Définition d'une liste statique de personnages fictifs
personnages = [
    {"nom": "Harry Potter", "univers": "Harry Potter"},
    {"nom": "Luke Skywalker", "univers": "Star Wars"}
]

# Définition du token secret requis pour accéder à l'API
TOKEN_SECRET = "super_token_123"

# Déclaration d’un endpoint GET accessible via l’URL /personnages
@app.get("/personnages")
def get_personnages(token: str = Header(None)):
    """
    Endpoint sécurisé par un token.
    L'utilisateur doit envoyer le bon token dans les headers pour accéder aux données.
    """
    # Vérification que le token transmis dans le header est correct
    if token != TOKEN_SECRET:
        # Si le token est incorrect ou manquant, on retourne une erreur 401 (Unauthorized)
        raise HTTPException(status_code=401, detail="Accès refusé : token invalide")
    
    # Si le token est valide, on retourne la liste des personnages
    return personnages
