import mysql.connector

# se connecter a la base de donnée
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme",
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f"Connecté à MySQL, version : {db_info}")

# exécuter des requêtes SQL
cursor = mydb.cursor()

# requête pour calculer la superficie totale des étage
cursor.execute("SELECT SUM(superficie) FROM etage")

# récuperer le résultat
resultat = cursor.fetchone()

# afficher le résultat
superficie_totale = resultat[0]
print(f"La superficie de La Plateforme est de {superficie_totale} m2")


cursor.close()
mydb.close()
