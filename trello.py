#Mini-Trello : Partie BOARDS avec option "Ouvrir un board" ===

trello = {"boards": []}

# Créer un board
def create_board(name):
    for board in trello["boards"]:
        if board["name"] == name:
            print("Board déjà existant.")
            return
    trello["boards"].append({"name": name, "lists": []})
    print(f"Board '{name}' créé.")

# Supprimer un board
def delete_board(name):
    trello["boards"] = [b for b in trello["boards"] if b["name"] != name]
    print(f"Board '{name}' supprimé.")

# Lister les boards
def list_boards():
    if not trello["boards"]:
        print("Aucun board existant.")
    else:
        print("Boards existants :")
        for board in trello["boards"]:
            print(f"- {board['name']}")

# Ouvrir un board
def open_board(name):
    for board in trello["boards"]:
        if board["name"] == name:
            print(f"\n=== Board : {name} ===")
            if not board["lists"]:
                print("Aucune liste dans ce board.")
            else:
                print("Listes :")
                for lst in board["lists"]:
                    print(f"- {lst['name']}")
            return
    print("Board non trouvé.")

# === Menu interactif ===
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

# Lancer le menu
menu()

