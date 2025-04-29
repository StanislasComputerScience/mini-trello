trello = {"boards": []}

def create_board(name):
    for board in trello["boards"]:
        if board["name"] == name:
            print("Board déjà existant.")
            return
    trello["boards"].append({"name": name, "lists": []})
    print(f"Board '{name}' créé")

create_board("Projet 1") 
create_board("Projet 2")

def delete_board(name):
    trello["boards"] = [b for b in trello["boards"] if b["name"] != name]
    print(f"Board '{name}' supprimé")

def list_boards():
    if not trello["boards"]:
        print("Aucun board existant")
    else:
        print("Boards existants :")
        for board in trello["boards"]:
            print(f"- {board['name']}")

list_boards()#voir boards existants
delete_board("Projet B")

#menu interactif
def menu():
    while True:
        print("\nMenu Mini-Trello")
        print("1. Créer un board")
        print("2. Supprimer un board")
        print("3. Lister les boards")
        print("4. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom du board : ")
            create_board(nom)
        elif choix == "2":
            nom = input("Nom du board à supprimer : ")
            delete_board(nom)
        elif choix == "3":
            list_boards_

menu()

#chaine vers tkinter