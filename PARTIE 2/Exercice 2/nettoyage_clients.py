import pandas as pd
import re

# Chargement du fichier CSV brut
df = pd.read_csv("clients_bruts.csv")

# Fonction de validation des emails
def est_email_valide(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Fonction de validation des codes postaux (on garde uniquement les codes à 5 chiffres)
def est_code_postal_valide(code):
    return str(code).isdigit() and len(str(code)) == 5

# Filtrage : on garde seulement les lignes valides
df_nettoye = df[
    df["email"].apply(est_email_valide) &
    df["code_postal"].apply(est_code_postal_valide)
]

# Sauvegarde du fichier nettoyé
df_nettoye.to_csv("clients_nettoyes.csv", index=False)
print("✅ Fichier nettoyé généré : clients_nettoyes.csv")
