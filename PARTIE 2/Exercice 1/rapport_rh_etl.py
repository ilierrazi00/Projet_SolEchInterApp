import pandas as pd

# Configuration
FICHIER_SORTIE = "rapport_candidatures.xlsx"

# Phase Extract (simulation de données locales)
def extract():
    # Simulation de candidatures reçues via une API RH
    return [
        {"nom": "Ahmed", "experience": 3, "email": "ahmed@mail.com"},
        {"nom": "Fatima", "experience": 1, "email": "fatima@mail.com"},
        {"nom": "Lina", "experience": 4, "email": "lina@mail.com"},
        {"nom": "Ziad", "experience": 0, "email": ""},
    ]

# Phase Transform (filtrage des profils intéressants)
def transform(data):
    profils_filtres = [
        c for c in data
        if c.get("experience", 0) >= 2 and c.get("email")
    ]
    return profils_filtres

# Phase Load (sauvegarde dans un fichier Excel)
def load(donnees_filtrees):
    df = pd.DataFrame(donnees_filtrees)
    df.to_excel(FICHIER_SORTIE, index=False)
    print(f"✅ Rapport généré avec {len(df)} profils : {FICHIER_SORTIE}")

# Exécution du mini-ETL
def run_etl():
    donnees = extract()
    donnees_filtrees = transform(donnees)
    load(donnees_filtrees)

if __name__ == "__main__":
    run_etl()
