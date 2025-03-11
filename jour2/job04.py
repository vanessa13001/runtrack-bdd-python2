import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parfait1313",
    database="LaPlateforme",
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f"Connecté à MySQL, version : {db_info}")

# création du curseur pour exécuter des requêtes SQL
cursor = mydb.cursor()

# exécution de la requête pour récupérer les noms et capacités de la table "salle"
cursor.execute("SELECT nom, capacite FROM salle")

# récuperer les resultats
salles = cursor.fetchall()

# afficher les résultats
print(" Liste des salles et leurs capacités :")
for salle in salles:
    print(f" Salle : {salle[0]} | Capacité : {salle[1]}")

# conexion fermer
cursor.close()
mydb.close()
