# === Partie 1 : Gestion des BOARDS ===

trello = {
    "boards": []
}

def create_board(name):
    for board in trello["boards"]:
        if board["name"] == name:
            print("Board déjà existant.")
            return
    trello["boards"].append({"name": name, "lists": []})
    print(f"Board '{name}' créé.")

def delete_board(name):
    trello["boards"] = [b for b in trello["boards"] if b["name"] != name]
    print(f"Board '{name}' supprimé.")

def list_boards():
    if not trello["boards"]:
        print("Aucun board existant.")
    else:
        print("Boards existants :")
        for board in trello["boards"]:
            print(f"- {board['name']}")

# === Tests de la partie BOARDS ===
create_board("Projet A")
create_board("Projet B")
list_boards()

delete_board("Projet B")
list_boards()
