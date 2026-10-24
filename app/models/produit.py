class Produit:
    def __init__(
        self,
        nom,
        prix,
        description,
        marque,
        image_url,
        image_locale,
        categorie,
        url_produit,
        image_blob=None
    ):
        self.nom = nom
        self.prix = prix
        self.description = description
        self.marque = marque
        self.image_url = image_url
        self.image_locale = image_locale
        self.categorie = categorie
        self.url_produit = url_produit
        self.image_blob = image_blob

    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Prix : {self.prix}")
        print(f"Description : {self.description}")
        print(f"Marque : {self.marque}")
        print(f"Image : {self.image_url}")
        print(f"Image locale : {self.image_locale}")
        print(f"Image enregistrée en base : {self.image_blob is not None}")
        print(f"Catégorie : {self.categorie}")
        print(f"URL du produit : {self.url_produit}")
