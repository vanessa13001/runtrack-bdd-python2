import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parfait1313",
    database="LaPlateforme",
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f"Connecté à MySQL, version : {db_info}")


cursor = mydb.cursor()
'''créer le curseur pour exécuter des requêtes SQL'''

cursor.execute("SELECT nom, capacite FROM salle")
'''exécution de la requête pour récupérer les noms et capacités de la table "salle"'''


salles = cursor.fetchall() 
''' la méthode fetchall récupère tous les résultats de la requête sous forme de liste de tuples'''

# afficher les résultats
print(" Liste des salles et leurs capacités :")
for salle in salles:
    print(f" Salle : {salle[0]} | Capacité : {salle[1]}")

# conexion fermer
cursor.close()
mydb.close()
