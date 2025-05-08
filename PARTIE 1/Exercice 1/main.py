# Importation du module principal de FastAPI
from fastapi import FastAPI

# Initialisation de l'application FastAPI
app = FastAPI()

# Définition d'une liste statique contenant deux personnages fictifs
personnages = [
    {"nom": "Harry Potter", "univers": "Harry Potter"},
    {"nom": "Luke Skywalker", "univers": "Star Wars"}
]

# Déclaration d'un endpoint GET accessible via l'URL /personnages
@app.get("/personnages")
def get_personnages():
    """
    Cette fonction est appelée lorsqu'une requête GET est envoyée à /personnages.
    Elle retourne une liste statique de personnages fictifs au format JSON.
    """
    return personnages
