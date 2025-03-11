import mysql.connector

class Zoo:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Parfait1313",
            database="zoo"
        )
        self.cursor = self.mydb.cursor()

    def fermer_connexion(self):
        self.cursor.close()
        self.mydb.close()

    def ajouter_cage(self, superficie, capacite_max):
        query = "insert into cage (superficie, capacite_max) values (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "insert into animal (nom, race, id_cage, date_naissance, pays_origine) values (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def afficher_animaux(self):
        query = "select a.id, a.nom, a.race, c.superficie, c.capacite_max from animal a join cage c on a.id_cage = c.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(f"id: {row[0]}, nom: {row[1]}, race: {row[2]}, cage superficie: {row[3]} m², capacité max: {row[4]}")

# exemple d'utilisation
zoo = Zoo()

# ajouter des cages
zoo.ajouter_cage(100, 5)
zoo.ajouter_cage(150, 10)

# ajouter des animaux
zoo.ajouter_animal("Lion", "Panthera leo", 1, "2015-08-01", "Afrique")
zoo.ajouter_animal("Elephant", "Loxodonta", 2, "2010-04-15", "Afrique")

# afficher les animaux et leur cage
zoo.afficher_animaux()

# fermer la connexion
zoo.fermer_connexion()
