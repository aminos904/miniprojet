import database
from file import FileAttente

class FileAttenteDAO:
    def __init__(self):
        self.connexion = database.connectDB()
        self.cursor = self.connexion.cursor()

    def ajouter(self, nom):
        try:
            file = FileAttente(nom)
            sql = "INSERT INTO filedattente (nom, priority) VALUES (%s, 0)"  # 0 pour personne normale
            values = (file.nom,)
            self.cursor.execute(sql, values)
            self.connexion.commit()
            print("Personne ajoutée à la file d'attente avec succès.")
        except Exception as error:
            print(f"Erreur lors de l'ajout à la file d'attente : {error}")

    def ajout_prioritaire(self, nom):
        try:
            file_attente = FileAttente(nom)
            sql = "INSERT INTO filedattente (nom, priority) VALUES (%s, 1)"  # 1 pour personne prioritaire
            values = (file_attente.nom,)
            self.cursor.execute(sql, values)
            self.connexion.commit()
            print("Personne prioritaire ajoutée à la file d'attente avec succès.")
        except Exception as error:
            print(f"Erreur lors de l'ajout d'une personne prioritaire à la file d'attente : {error}")

    def supprimer(self):
        try:
            # Priorité aux personnes prioritaires
            sql_prioritaire = "DELETE FROM filedattente WHERE priority = 1 ORDER BY id ASC LIMIT 1"
            self.cursor.execute(sql_prioritaire)
            if self.cursor.rowcount > 0:
                print("Personne prioritaire retirée de la file d'attente.")
            else:
                # Si pas de personne prioritaire, retirer une personne normale
                sql_normale = "DELETE FROM filedattente WHERE priority = 0 ORDER BY id ASC LIMIT 1"
                self.cursor.execute(sql_normale)
                if self.cursor.rowcount > 0:
                    print("Personne retirée de la file d'attente.")
                else:
                    print("File d'attente vide.")
            self.connexion.commit()
        except Exception as error:
            print(f"Erreur lors de la suppression de personne de la file d'attente : {error}")

    def afficher(self):
        try:
            sql = "SELECT nom, priority FROM filedattente ORDER BY priority DESC, id ASC"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if not results:
                print("File d'attente vide.")
            else:
                print("Personnes dans la file d'attente :")
                for result in results:
                    priority = "prioritaire" if result[1] == 1 else "normal"
                    print(f"{result[0]} ({priority})")
        except Exception as error:
            print(f"Erreur lors de l'affichage de la file d'attente : {error}")
