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
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def supprimer_animal(self, id_animal):
        query = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(query, (id_animal,))
        self.mydb.commit()

    def supprimer_cage(self, id_cage):
        query = "DELETE FROM cage WHERE id = %s"
        self.cursor.execute(query, (id_cage,))
        self.mydb.commit()

    def afficher_animaux(self):
        query = "SELECT a.id, a.nom, a.race, c.superficie, c.capacite_max FROM animal a JOIN cage c ON a.id_cage = c.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("liste des animaux présents dans le zoo :")
        for row in result:
            print(f"ID: {row[0]}, Nom: {row[1]}, Race: {row[2]}, Cage Superficie: {row[3]} m², Capacité Max: {row[4]}")

    def afficher_animaux_par_cage(self):
        query = """
        SELECT c.id, c.superficie, a.nom, a.race 
        FROM cage c
        LEFT JOIN animal a ON c.id = a.id_cage
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("liste des animaux dans chaque cage :")
        for row in result:
            if row[2]:  # Si un animal est présent dans la cage
                print(f"Cage ID: {row[0]}, Superficie: {row[1]} m², Animal: {row[2]} ({row[3]})")
            else:
                print(f"Cage ID: {row[0]}, Superficie: {row[1]} m², Cage vide")

    def superficie_totale_cages(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        print(f"la superficie totale de toutes les cages est de {result[0]} m².")

    def menu(self):
        while True:
            print("\nmenu du zoo :")
            print("1. ajouter un animal")
            print("2. ajouter une cage")
            print("3. supprimer un animal")
            print("4. supprimer une cage")
            print("5. afficher les animaux")
            print("6. afficher les animaux par cage")
            print("7. calculer la superficie totale des cages")
            print("8. quitter")

            choix = input("que voulez-vous faire ? (1-8): ")

            if choix == '1':
                nom = input("nom de l'animal : ")
                race = input("race de l'animal : ")
                id_cage = int(input("ID de la cage : "))
                date_naissance = input("date de naissance (YYYY-MM-DD) : ")
                pays_origine = input("pays d'origine de l'animal : ")
                self.ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)
            elif choix == '2':
                superficie = int(input("superficie de la cage (en m²) : "))
                capacite_max = int(input("capacité maximale de la cage : "))
                self.ajouter_cage(superficie, capacite_max)
            elif choix == '3':
                id_animal = int(input("ID de l'animal à supprimer : "))
                self.supprimer_animal(id_animal)
            elif choix == '4':
                id_cage = int(input("ID de la cage à supprimer : "))
                self.supprimer_cage(id_cage)
            elif choix == '5':
                self.afficher_animaux()
            elif choix == '6':
                self.afficher_animaux_par_cage()
            elif choix == '7':
                self.superficie_totale_cages()
            elif choix == '8':
                print("au revoir !")
                break
            else:
                print("choix invalide, veuillez entrer un numéro entre 1 et 8.")

# Exemple d'utilisation
zoo = Zoo()
zoo.menu()
zoo.fermer_connexion()
