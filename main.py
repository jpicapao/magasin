from statistics import quantiles

from Employes import *
from Produits import *

def add_employe():
    ID = input("votre ID: ")
    nom = input("notez votre nom: ")
    prenom = input("notez votre prenom: ")
    age = int(input("notez votre age: "))
    adresse = input("notez votre adresse: ")

    liste_employes[ID] = Employe(ID, nom, prenom, age, adresse)

def add_product():
    ID_p = input("notez l'ID du produit: ")

    if ID_p in liste_produits:
        print("votre produit existe déjà")
        return
    try:
        nom = input("notez le nom du produit: ")
        categorie = input("notez la catégorie du produit: ")
        prix = float(input("notez le prix à l'unité du produit: "))
        stock = int(input("notez le stock du nouveau produit: "))

    except Exception:
        print("votre saisie n'a pas pu être prise en compte")
        return


    liste_produits[ID_p] = Produit(ID_p, nom, categorie, prix, stock)



def main():
    while True:
        print("Bienvenu dans votre Magasin préféré:")
        print("             HELLO WORLD        ")

        print("êtes vous un nouvel employé ?")
        answer = input("Y/N: ")

        while answer.lower() !=  "y" and answer.lower() !=  "n":
            print("votre réponse doit être Y ou N.")
            print("êtes vous un nouvel employé ?")
            answer = input("Y/N: ")

        if answer.lower() == "y":
            add_employe()


        print("veuillez vous identifier")
        employe_ID = input("ID: ")

        if employe_ID in liste_employes:
            print(f"Bienvenue M/Mme {liste_employes[employe_ID].nom}")
        else:
            print("Vous n'êtes pas reconnu")
            continue

        while True:
            print("MENU:")
            print("1. ajout nouveau produit")
            print("2. consulter produit")
            print("3. ajout quantité produit")
            print("4. quitter")

            choix = int(input("Votre choix: "))

            while choix not in (1, 2, 3, 4):
                print("réponse incorrecte, veuillez écrire un nombre entre 1 et 4")
                choix = int(input("Votre choix: "))

            if choix == 1:
                add_product()
            elif choix == 2:
                ID_produit = input("ID du produit: ")

                if ID_produit not in liste_produits:
                    print("Ce produit n'existe pas")
                    continue


                liste_produits[ID_produit].affichage()
            elif choix == 3:
                ID_produit = input("ID du produit: ")

                if ID_produit not in liste_produits:
                    print("Ce produit n'existe pas")
                    continue

                print("Quelle quantité voulez-vous ajouter?")

                quantite = int(input("quantité: "))
                liste_produits[ID_produit].add_stock(quantite)
            else:
                print("Déconnexion")
                break



liste_employes = {}
liste_produits = {}

main()