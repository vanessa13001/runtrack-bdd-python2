import mysql.connector

class Zoo:
    '''l'option ( fonction)  charset spécifie le jeu de caractères utilisé pour l'encodage des données échangées entre le client (ton script Python) et la base de données'''
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Parfait1313",
            database="zoo",
            charset="utf8mb4"  # charset pour éviter les problèmes d'encodage
        )
        '''mon charset=utf8mb4, signifie que la connexion utilisera UTF-8 en 4 octets, c'est une version améliorée de UTF-8 permettant de stocker des caractères spéciaux comme les emojis et certains caractères asiatiques'''
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
        try:
            # on valide que le pays d'origine n'est pas vide
            pays_origine = pays_origine.strip()
            if not pays_origine:
                print("Le pays d'origine ne peut pas être vide.")
                return

            # on verifie si l'id de la cage existe
            self.cursor.execute("SELECT id FROM cage WHERE id = %s", (id_cage,))
            result = self.cursor.fetchone()
            if result is None:
                print(f"L'ID de la cage {id_cage} n'existe pas dans la base de données.")
                return

            query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
            values = (nom, race, id_cage, date_naissance, pays_origine)
            self.cursor.execute(query, values)
            self.mydb.commit()
            print("Animal ajouté avec succès!")
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'ajout de l'animal: {err}")

    def supprimer_animal(self, id_animal):
        '''query est une chaîne de caractères qui stocke la requête SQL avant son exécution'''

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
        print("Liste des animaux présents dans le zoo :")
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
        print("Liste des animaux dans chaque cage :")
        for row in result:
            if row[2]:  # si un animal est présent dans la cage
                print(f"Cage ID: {row[0]}, Superficie: {row[1]} m², Animal: {row[2]} ({row[3]})")
            else:
                print(f"Cage ID: {row[0]}, Superficie: {row[1]} m², Cage vide")

    def superficie_totale_cages(self):
        ''' La fonction SUM calcule la somme totale des valeurs dans la colonne superficie.'''
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        print(f"La superficie totale de toutes les cages est de {result[0]} m².")

    def menu(self):
        while True:
            print("\nMenu du zoo :")
            print("1. Ajouter un animal")
            print("2. Ajouter une cage")
            print("3. Supprimer un animal")
            print("4. Supprimer une cage")
            print("5. Afficher les animaux")
            print("6. Afficher les animaux par cage")
            print("7. Calculer la superficie totale des cages")
            print("8. Quitter")

            choix = input("Que voulez-vous faire ? (1-8): ")

            if choix == '1':
                nom = input("Nom de l'animal : ")
                race = input("Race de l'animal : ")
                id_cage = int(input("ID de la cage : "))
                date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
                pays_origine = input("Pays d'origine de l'animal : ")
                self.ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)
            elif choix == '2':
                superficie = int(input("Superficie de la cage (en m²) : "))
                capacite_max = int(input("Capacité maximale de la cage : "))
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
                print("Au revoir !")
                break
            else:
                print("Choix invalide, veuillez entrer un numéro entre 1 et 8.")


zoo = Zoo()
zoo.menu()
zoo.fermer_connexion()
