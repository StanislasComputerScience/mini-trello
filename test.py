#Un seul "board"
board = {
    "nom": "Mon projet Trello",
    "listes": []
}

#Ajouter une liste
def ajouter_liste(nom_liste):
    nouvelle_liste = {
        "nom": nom_liste,
        "cartes": []
    }
    board["listes"].append(nouvelle_liste)
    print(f"Liste '{nom_liste}' ajoutée.")

#Afficher les listes
def afficher_listes():
    print("\nListes dans le board :")
    for liste in board["listes"]:
        print(f"- {liste['nom']}")

#Ajouter une carte dans une liste
def ajouter_carte(nom_liste, titre_carte):
    for liste in board["listes"]:
        if liste["nom"] == nom_liste:
            liste["cartes"].append(titre_carte)
            print(f"Carte '{titre_carte}' ajoutée à la liste '{nom_liste}'.")
            return
    print("Liste non trouvée.")

#Afficher les cartes d’une liste
def afficher_cartes(nom_liste):
    for liste in board["listes"]:
        if liste["nom"] == nom_liste:
            print(f"\nCartes dans '{nom_liste}':")
            for carte in liste["cartes"]:
                print(f"- {carte}")
            return
    print("Liste non trouvée.")

#Exemple d'utilisation simple

ajouter_liste("À faire")
ajouter_liste("En cours")

afficher_listes()

ajouter_carte("À faire", "Écrire le code")
ajouter_carte("À faire", "Relire les consignes")

afficher_cartes("À faire")


# mini_trello.py — version sans fichiers, en mémoire avec des dictionnaires

# Base de données en mémoire
trello = {
    "boards": []
}

# === BOARDS ===

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
    print("Boards existants :")
    for board in trello["boards"]:
        print(f"- {board['name']}")

def get_board(name):
    for board in trello["boards"]:
        if board["name"] == name:
            return board
    return None

# === LISTS ===

def add_list(board_name, list_name):
    board = get_board(board_name)
    if board:
        for lst in board["lists"]:
            if lst["name"] == list_name:
                print("Liste déjà existante.")
                return
        board["lists"].append({"name": list_name, "cards": []})
        print(f"Liste '{list_name}' ajoutée au board '{board_name}'.")
    else:
        print("Board non trouvé.")

def delete_list(board_name, list_name):
    board = get_board(board_name)
    if board:
        board["lists"] = [lst for lst in board["lists"] if lst["name"] != list_name]
        print(f"Liste '{list_name}' supprimée du board '{board_name}'.")
    else:
        print("Board non trouvé.")

def list_lists(board_name):
    board = get_board(board_name)
    if board:
        print(f"Listes dans le board '{board_name}':")
        for lst in board["lists"]:
            print(f"- {lst['name']}")
    else:
        print("Board non trouvé.")

def get_list(board, list_name):
    for lst in board["lists"]:
        if lst["name"] == list_name:
            return lst
    return None

# === CARDS ===

def add_card(board_name, list_name, card_title):
    board = get_board(board_name)
    if board:
        lst = get_list(board, list_name)
        if lst:
            lst["cards"].append(card_title)
            print(f"Carte '{card_title}' ajoutée à la liste '{list_name}'.")
        else:
            print("Liste non trouvée.")
    else:
        print("Board non trouvé.")

def delete_card(board_name, list_name, card_title):
    board = get_board(board_name)
    if board:
        lst = get_list(board, list_name)
        if lst and card_title in lst["cards"]:
            lst["cards"].remove(card_title)
            print(f"Carte '{card_title}' supprimée.")
        else:
            print("Carte ou liste non trouvée.")
    else:
        print("Board non trouvé.")

def move_card(board_name, source_list, target_list, card_title):
    board = get_board(board_name)
    if board:
        src = get_list(board, source_list)
        tgt = get_list(board, target_list)
        if src and tgt and card_title in src["cards"]:
            src["cards"].remove(card_title)
            tgt["cards"].append(card_title)
            print(f"Carte '{card_title}' déplacée de '{source_list}' à '{target_list}'.")
        else:
            print("Erreur : carte ou listes non trouvées.")
    else:
        print("Board non trouvé.")

def list_cards(board_name, list_name):
    board = get_board(board_name)
    if board:
        lst = get_list(board, list_name)
        if lst:
            print(f"Cartes dans la liste '{list_name}':")
            for card in lst["cards"]:
                print(f"- {card}")
        else:
            print("Liste non trouvée.")
    else:
        print("Board non trouvé.")

# === EXEMPLE ===

if __name__ == "__main__":
    create_board("Projet A")
    add_list("Projet A", "À faire")
    add_list("Projet A", "En cours")
    add_card("Projet A", "À faire", "Écrire le code")
    add_card("Projet A", "À faire", "Corriger les bugs")
    list_boards()
    list_lists("Projet A")
    list_cards("Projet A", "À faire")
    move_card("Projet A", "À faire", "En cours", "Corriger les bugs")
    list_cards("Projet A", "En cours")
