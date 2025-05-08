import pandas as pd
import sqlite3

# Lecture du fichier CSV
df = pd.read_csv("logs.csv")

# Connexion à une base SQLite temporaire
conn = sqlite3.connect("logs_banque.db")
df.to_sql("logs", conn, if_exists="replace", index=False)

# Analyse SQL : nombre d’actions par utilisateur
requete = """
SELECT utilisateur, COUNT(*) as total_actions, 
       SUM(CASE WHEN statut != 200 THEN 1 ELSE 0 END) as erreurs
FROM logs
GROUP BY utilisateur
ORDER BY total_actions DESC;
"""

resultat = pd.read_sql_query(requete, conn)
print(resultat)

# Sauvegarde de l'analyse
resultat.to_csv("analyse_logs.csv", index=False)
print("✅ Analyse sauvegardée dans 'analyse_logs.csv'")
