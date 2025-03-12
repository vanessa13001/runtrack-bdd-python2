import mysql.connector

class Employe:
    def __init__(self, id=None, nom=None, prenom=None, salaire=None, id_service=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    def connecter(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="LaPlateforme"
        )
        self.cursor = self.mydb.cursor()

    def fermer_connexion(self):
        self.cursor.close()
        self.mydb.close()

    '''CRUD est un acronyme des noms des quatre opérations de base de la gestion de la persistance des données et applications 
    Create
    Read
    Update
    Delete
    le CRUD résume les fonctions qu'un utilisateur a besoin d'utiliser pour créer et gérer des données
    '''

    # create - ajouter un employé
    def ajouter_employe(self):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (self.nom, self.prenom, self.salaire, self.id_service)
        self.cursor.execute(query, values)
        self.mydb.commit() # commit validation des modifications

    # read - récupérer tous les employés
    def afficher_employes(self):
        '''e.id, e.nom, e.prenom, e.salaire => Colonnes de la table employe (raccourcie en e).'''
    
        self.cursor.execute("SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS service FROM employe e JOIN service s ON e.id_service = s.id")

        '''s.nom AS service => Colonne nom de la table service (raccourcie en s), renommée service dans les résultats.'''

        result = self.cursor.fetchall()
        for row in result:
            print(f"ID: {row[0]}, Nom: {row[1]}, Prénom: {row[2]}, Salaire: {row[3]} €, Service: {row[4]}")

    # update - mettre à jour un employé
    def mettre_a_jour_employe(self):
        query = "UPDATE employe SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        values = (self.nom, self.prenom, self.salaire, self.id_service, self.id)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def supprimer_employe(self):
        query = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(query, (self.id,))
        self.mydb.commit()

# exemple d'utilisation
employe1 = Employe(nom="Dupont", prenom="Jean", salaire=3500, id_service=1)
employe1.connecter()
employe1.ajouter_employe()
employe1.afficher_employes()

# mettre à jour un employé
employe1.id = 1
employe1.nom = "Dupont"
employe1.prenom = "Jean-Paul"
employe1.salaire = 4000
employe1.mettre_a_jour_employe()


employe1.afficher_employes()


employe1.supprimer_employe()


employe1.afficher_employes()

employe1.fermer_connexion()
