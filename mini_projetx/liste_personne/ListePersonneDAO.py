import database
from ListePersonne import Personne

class PersonneDAO:
    def __init__(self):
        self.connexion = database.connectDB()
        self.cursor = self.connexion.cursor()

    def ajouter_personne(self, personne):
        try:
            sql = "INSERT INTO Personnes (nom, age) VALUES (%s, %s)"
            values = (personne.nom, personne.age)
            self.cursor.execute(sql, values)
            self.connexion.commit()
            print("Nouvelle personne ajoutée avec succès.")
        except Exception as error:
            print(f"Erreur lors de l'ajout de la personne : {error}")

    def chercher_personne(self, nom):
        try:
            sql = "SELECT nom, age FROM Personnes WHERE nom = %s"
            self.cursor.execute(sql, (nom,))
            result = self.cursor.fetchone()
            if result:
                return Personne(result[0], result[1])
            else:
                print("Personne non trouvée dans la base de données.")
                return None
        except Exception as error:
            print(f"Erreur lors de la recherche de la personne : {error}")

    def mettre_a_jour_personne(self, personne, nouvel_age):
        try:
            sql = "UPDATE Personnes SET age = %s WHERE nom = %s"
            values = (nouvel_age, personne.nom())
            self.cursor.execute(sql, values)
            self.connexion.commit()
            print("Âge de la personne mis à jour avec succès.")
        except Exception as error:
            print(f"Erreur lors de la mise à jour de l'âge de la personne : {error}")

    def supprimer_personne(self, nom):
        try:
            sql = "DELETE FROM Personnes WHERE nom = %s"
            self.cursor.execute(sql, (nom,))
            self.connexion.commit()
            print("Personne supprimée avec succès.")
        except Exception as error:
            print(f"Erreur lors de la suppression de la personne : {error}")

    def filtrer_par_age(self, age_min, age_max):
        try:
            sql = "SELECT nom, age FROM Personnes WHERE age >= %s AND age <= %s"
            self.cursor.execute(sql, (age_min, age_max))
            results = self.cursor.fetchall()
            personnes_filtrees = []
            for result in results:
                personnes_filtrees.append(Personne(result[0], result[1]))
            return personnes_filtrees
        except Exception as error:
            print(f"Erreur lors du filtrage par âge : {error}")
            return []

