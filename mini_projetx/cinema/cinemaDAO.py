"""
l'imporation de Cinema ne veut pas fonctionné. j'ai esseiller plusieur solution est c'est toujours le meme probleme.
"""

import database
from cinema import Cinema

class CinemaDAO:
    def __init__(self):
        self.connexion = database.connectDB()
        self.cursor = self.connexion.cursor()

    def reserver_place(self, nom, places):
        try:
            salle = Cinema(capacite=50, special=5)  
            salle.reserver_place(nom, places)  
        except Exception as error:
            print(f"Erreur lors de la réservation : {error}")

    def reserver_place_speciale(self, nom):
        try:
            salle = Cinema(capacite=50, special=5) 
            salle.reserver_place_speciale(nom)  
        except Exception as error:
            print(f"Erreur lors de la réservation d'une place spéciale : {error}")

    def afficher_places_reservees(self,):
        try:
            sql = "SELECT nom, places, speciale FROM reservation"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if not results:
                print("Aucune réservation trouvée.")
            else:
                print("Liste des réservations :")
                for result in results:
                    nom = result[0]
                    places = result[1]
                    type_reservation = "place spéciale" if result[2] else "place normale"
                    print(f"{nom} a réservé {places} {type_reservation}")
        except Exception as error:
            print(f"Erreur lors de l'affichage des réservations : {error}")

    def annuler_reservation(self, nom):
        try:
            sql = "DELETE FROM reservation WHERE nom = %s"
            self.cursor.execute(sql, (nom,))
            self.connexion.commit()
            if self.cursor.rowcount > 0:
                print(f"Réservations de {nom} annulées avec succès.")
            else:
                print(f"Aucune réservation trouvée pour {nom}.")
        except Exception as error:
            print(f"Erreur lors de l'annulation des réservations : {error}")