from typing import *

def ajouter_tache(dico : dict , *nom_tache:str) -> dict:
    n = len(dico)
    print(type(nom_tache))
    for nom in nom_tache:
        dico[len(dico)] = nom
        n += 1
    return dico

def supprimer_tache(dico: dict, nom: str) -> dict:
    # Supprime toutes les entrées dont la valeur correspond au nom donné
    keys_to_delete = [k for k, v in dico.items() if v == nom]
    for k in keys_to_delete:
        del dico[k]
    return dico


def run_card():
    d = dict()
    t = "Tailler mon crayon", "ranger ma chambre", "tondre la pelouse", "aller à Basic Fit", " Creer un générateur de snipet"
    Cartes = ajouter_tache(d,*t)
    print(type(Cartes))
    print(Cartes)

    supprimer_tache(d,"ranger ma chambre")
    print(d)
    ajouter_tache(d,"seb ", "Anice")
    print(d)
if __name__ == '__main__':
    run_card()
