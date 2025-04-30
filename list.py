from card import ajouter_tache
from card import supprimer_tache

d = dict()
t = "Tailler mon crayon", "ranger ma chambre", "tondre la pelouse", "aller à Basic Fit", " Creer un générateur de snipet"
Cartes = ajouter_tache(d,*t)

def creer_list(nom : str, *num_tache:str):
    d = dict()
    d["nom de la liste"] = nom
    d["liste num_tache"] = [num for num in num_tache]
    return d

d = creer_list("Première liste",1,2,3)
print(d)
print ("c,wxkl,cwxmkl")
print(Cartes)
