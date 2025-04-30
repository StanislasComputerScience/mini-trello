def menu():
    while True:
        print("\n=== Menu Mini-Trello ===")
        print("1. Créer un board")
        print("2. Supprimer un board")
        print("3. Lister les boards")
        print("4. Ouvrir un board")
        print("5. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom du board : ")
            create_board(nom)
        elif choix == "2":
            nom = input("Nom du board à supprimer : ")
            delete_board(nom)
        elif choix == "3":
            list_boards()
        elif choix == "4":
            nom = input("Nom du board à ouvrir : ")
            open_board(nom)
        elif choix == "5":
            print("À bientôt !")
            break
        else:
            print("Choix invalide.")
if __name__ == "__main__":
    menu()