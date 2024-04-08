from salle_cinema_dao import SalleCinemaDAO
from salle import Salle

salle_cinema_dao = SalleCinemaDAO()

while True:
    print("\nTapez 1 pour réserver une place normale.")
    print("Tapez 2 pour réserver une place spéciale.")
    print("Tapez 3 pour afficher le nombre de places disponibles.")
    print("Tapez 4 pour filtrer les réservations par personne.")
    print("Tapez 5 pour annuler les réservations d'une personne.")
    print("Tapez 6 pour quitter.")

    option = input("\nEntrez l'option choisie : ")

    if option == "1":
        nom_personne = input("Entrez le nom de la personne : ")
        places_reserver = int(input("Entrez le nombre de places à réserver : "))
        salle_cinema_dao.reserver_place(nom_personne, places_reserver)
    elif option == "2":
        nom_personne_speciale = input("Entrez le nom de la personne pour la place spéciale : ")
        salle_cinema_dao.reserver_place_speciale(nom_personne_speciale)
    elif option == "3":
        print(f"Nombre de places disponibles : {salle_cinema_dao.nombre_places_disponibles()}")
    elif option == "4":
        nom_filtre = input("Entrez le nom de la personne pour filtrer les réservations : ")
        salle_cinema_dao.filtrer_reservations_par_personne(nom_filtre)
    elif option == "5":
        nom_annulation = input("Entrez le nom de la personne pour annuler les réservations : ")
        salle_cinema_dao.annuler_reservation(nom_annulation)
    elif option == "6":
        break
    else:
        print("Option invalide")

