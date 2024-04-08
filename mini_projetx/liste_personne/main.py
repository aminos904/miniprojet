from ListePersonneDAO import PersonneDAO
from ListePersonne import Personne

personne_dao = PersonneDAO()

5

while True:
    
    print("\nTapez 1 pour ajouter une personne.")
    print("Tapez 2 pour chercher une personne.")
    print("Tapez 3 pour mettre à jour l'âge d'une personne.")
    print("Tapez 4 pour supprimer une personne.")
    print("Tapez 5 pour filtrer les personnes par âge.")
    print("Tapez 'q' pour quitter.")
    option = input("\nEntrez l'option choisie : ")

    if option == "1":
        nom = input("\nEntrez le nom de la personne à ajouter : ")
        age = int(input("Entrez l'âge de la personne : "))
        nouvelle_personne = Personne(nom, age)
        personne_dao.ajouter_personne(nouvelle_personne)

    elif option == "2":
        nom_recherche = input("\nEntrez le nom de la personne recherchée : ")
        personne_trouvee = personne_dao.chercher_personne(nom_recherche)
        if personne_trouvee:
            print(f"Personne trouvée : {personne_trouvee.nom}, Âge : {personne_trouvee.age}")

    elif option == "3":
        nom = input("\nEntrez le nom de la personne à mettre à jour : ")
        nouvel_age = int(input("Entrez le nouvel âge : "))
        personne_dao.mettre_a_jour_personne(Personne(nom, 0), nouvel_age)  # Crée une personne temporaire avec l'âge 0 pour la mise à jour

    elif option == "4":
        nom = input("\nEntrez le nom de la personne à supprimer : ")
        personne_dao.supprimer_personne(nom)

    elif option == "5":
        age_min = int(input("\nEntrez l'âge minimum : "))
        age_max = int(input("Entrez l'âge maximum : "))
        personnes_filtrees = personne_dao.filtrer_par_age(age_min, age_max)
        print("Personnes filtrées par âge :")
        for personne in personnes_filtrees:
            print(f"Nom : {personne.nom}, Âge : {personne.age}")

    elif option.lower() == "q":
        break

    else:
            print("Option invalide. Veuillez réessayer.")
