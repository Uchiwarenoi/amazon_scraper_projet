from app.scraper_utile.amazon_scraper import AmazonScraper
from app.models.depot import Depot
from app.models.produit import Produit
from app.views.export_view import ExportView

class ScrapingController:
    def __init__(self):
        self.scraper = AmazonScraper()
        self.depot = Depot()

    def verifier_site(self, url):
        if not url.startswith(("http://", "https://")):
            print("Adresse invalide.")
            return False
        return self.scraper.verifier_acces(url)

    def obtenir_produits(self):
        return self.depot.obtenir_tous()

    def rechercher_marque(self, marque):
        return self.depot.rechercher_par_marque(marque)

    def compter_produits(self):
        return self.depot.compter_produits()

    def ajouter_produit(self, donnees):
        nom = donnees.get("nom", "").strip()
        if not nom:
            print("Le nom du produit est obligatoire.")
            return False
        try:
            texte = str(donnees.get("prix", "")).strip()
            prix = float(texte.replace(",", ".")) if texte else None
        except ValueError:
            print("Le prix doit être un nombre valide.")
            return False
        produit = Produit(nom, prix, donnees.get("description", ""), donnees.get("marque", ""),
                          donnees.get("image_url", ""), donnees.get("image_locale", ""),
                          donnees.get("categorie", ""), donnees.get("url_produit", ""))
        return self.depot.ajouter_produit(produit)

    @staticmethod
    def _convertir_prix(prix):
        if not prix or prix == "Non disponible":
            return None
        texte = str(prix).replace("$", "").replace(",", "").strip()
        try:
            return float(texte)
        except ValueError:
            return None

    def scraper_recherche(self, recherche, categorie):
        resultats = self.scraper.rechercher_produits(recherche, categorie, limite=20)
        enregistres = 0
        for d in resultats:
            produit = Produit(d["nom"], self._convertir_prix(d["prix"]), d["description"], d["marque"],
                              d["image_url"], d["image_locale"], d["categorie"], d["url_produit"])
            if self.depot.ajouter_produit(produit):
                enregistres += 1
        if resultats:
            print(f"Produits trouvés : {len(resultats)}")
            print(f"Nouveaux produits enregistrés : {enregistres}")
        return resultats

    def exporter_produits(self):
        return ExportView().exporter_csv(self.depot.obtenir_tous())
