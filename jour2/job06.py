import mysql.connector

# connexion à la base de données
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

# exécution de la requête pour calculer la capacité totale des salles
cursor.execute("SELECT SUM(capacite) FROM salle")

# récupération du résultat
resultat = cursor.fetchone()

# afficher le résultat
capacite_totale = resultat[0]
print(f"La capacité totale des salles est de {capacite_totale} personnes")

# la conexion est fermée
cursor.close()
mydb.close()
