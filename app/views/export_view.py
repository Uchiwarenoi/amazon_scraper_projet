import csv
from pathlib import Path

from config import DOSSIER_EXPORTS


class ExportView:
    def exporter_csv(self, produits, nom_fichier="produits.csv"):
        chemin = Path(DOSSIER_EXPORTS) / nom_fichier

        colonnes = [
            "id",
            "nom",
            "prix",
            "description",
            "marque",
            "image_url",
            "image_locale",
            "categorie",
            "url_produit"
        ]

        with open(chemin, "w", newline="", encoding="utf-8-sig") as fichier:
            writer = csv.writer(fichier, delimiter=";")
            writer.writerow(colonnes)
            writer.writerows(produits)

        return chemin
