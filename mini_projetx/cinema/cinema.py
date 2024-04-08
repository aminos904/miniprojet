class Cinema:
    def __init__(self, capacite, special):
        self.__capacite = capacite
        self.__disponibles = capacite
        self.__special = special

    @property
    def capacite(self):
        return self.__capacite

    @property
    def disponibles(self):
        return self.__disponibles

    @property
    def special(self):
        return self.__special

    def reserver_place(self, nom, places):
        if places > self.__disponibles:
            print("Pas assez de places disponibles !")
        else:
            self.__disponibles -= places
            print(f"Réservation effectuée pour {places} place(s) au nom de {nom}.")

    def reserver_place_speciale(self, nom):
        if self.__special > 0:
            self.__special -= 1
            print(f"Place spéciale réservée pour {nom}.")
        else:
            print("Désolé, il n'y a plus de places spéciales disponibles.")
