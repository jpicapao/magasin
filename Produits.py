class Produit:
    def __init__(self, IDProduit, nom, categorie, prix, stock):
        self.IDProduit = IDProduit
        self.nom = nom
        self.categorie = categorie
        self.prix = prix
        self.stock = stock


    def affichage(self):
        print(f"IDProduit: {self.IDProduit}, nom: {self.nom}, catégorie: {self.categorie}, prix: {self.prix}, stock: {self.stock}")


    def add_stock(self, quantite):
        self.stock += quantite