"""
l'imporation de Cinema ne veut pas fonctionné. j'ai esseiller plusieur solution est c'est toujours le meme probleme.
"""
from cinemaDAO import CinemaDAO
from cinema import Cinema

cine_dao = CinemaDAO()

while True:
    print("\nTapez 1 pour réserver une place normale.")
    print("Tapez 2 pour réserver une place spéciale.")
    print("Tapez 3 pour afficher le nombre de places disponibles.")
    print("Tapez 4 pour afficher les réservations effectuées.")
    print("Tapez 5 pour annuler une rervation.")
    print("Tapez q pour quitter.")

    option = input("\nEntrez l'option choisie : ")

    if option == "1":
        nom_personne = input("Entrez le nom de la personne : ")
        places_reserver = int(input("Entrez le nombre de places à réserver : "))
        cine_dao.reserver_place(nom_personne, places_reserver)

    elif option == "2":
        nom_personne_speciale = input("Entrez le nom de la personne pour la place spéciale : ")
        cine_dao.reserver_place_speciale(nom_personne_speciale)

    elif option == "3":
        cine_dao.afficher_places_reservees()

    elif option == "4":
        cine_dao.afficher_places_reservees()

    elif option == "5":
        cine_dao.annuler_reservation()

    elif option == "q":
        break

    else:
        print("Option invalide.")
