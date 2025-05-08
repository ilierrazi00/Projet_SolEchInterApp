import sqlite3
import pandas as pd

# Connexion à la base SQLite
conn = sqlite3.connect("ecommerce.db")

# Requête 1 : Nombre de commandes par client
req_commandes_par_client = """
SELECT client, COUNT(*) AS total_commandes
FROM commandes
GROUP BY client
"""

# Requête 2 : Montant total des commandes par client
req_montant_par_client = """
SELECT client, SUM(montant) AS total_depense
FROM commandes
GROUP BY client
"""

# Requête 3 : Commandes les plus récentes
req_commandes_recentes = """
SELECT *
FROM commandes
ORDER BY date DESC
LIMIT 5
"""

# Exécution des requêtes et création de DataFrames
df_commandes = pd.read_sql_query(req_commandes_par_client, conn)
df_montant = pd.read_sql_query(req_montant_par_client, conn)
df_recentes = pd.read_sql_query(req_commandes_recentes, conn)

# Fusion des DataFrames 1 et 2
df_global = pd.merge(df_commandes, df_montant, on="client")

# Export dans un fichier Excel
with pd.ExcelWriter("reporting_ecommerce.xlsx") as writer:
    df_global.to_excel(writer, sheet_name="Synthèse", index=False)
    df_recentes.to_excel(writer, sheet_name="Récent", index=False)

print("✅ Rapport 'reporting_ecommerce.xlsx' généré avec succès.")
