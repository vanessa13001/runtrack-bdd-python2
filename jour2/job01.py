import mysql.connector

# Connexion à la base de données
mydb  = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme",
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f"Connecté à MySQL, version : {db_info}")


cursor = mydb.cursor()
cursor.execute("SELECT * FROM etudiant")


etudiant = cursor.fetchall()

for etudiant in etudiant:
    print(etudiant)

# Fermeture de la connexion
cursor.close()
mydb.close()
