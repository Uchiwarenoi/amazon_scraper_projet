from app.controllers.scraping_controller import ScrapingController
from app.views.console_view import ConsoleView

def main():
    vue = ConsoleView()
    controleur = ScrapingController()
    while True:
        vue.afficher_menu()
        choix = vue.demander_choix()
        if choix == "1":
            selection = vue.demander_sous_categorie_tech()
            if selection:
                categorie, recherche = selection
                vue.afficher_resultats_scraping(controleur.scraper_recherche(recherche, categorie))
        elif choix == "2":
            recherche = vue.demander_categorie_libre()

            if recherche is not None:
                produits = controleur.scraper_recherche(
                    recherche,
                    "Autres"
                )
                vue.afficher_resultats_scraping(produits)
        elif choix == "3":
            vue.afficher_produits(controleur.obtenir_produits())
        elif choix == "4":
            vue.afficher_produits(controleur.rechercher_marque(vue.demander_marque()))
        elif choix == "5":
            vue.afficher_message(f"Nombre de produits enregistrés : {controleur.compter_produits()}")
        elif choix == "6":
            if controleur.ajouter_produit(vue.demander_produit()):
                vue.afficher_message("Produit enregistré.")
            else:
                vue.afficher_message("Produit non enregistré (doublon ou données invalides).")
        elif choix == "7":
            vue.afficher_export(controleur.exporter_produits())
        elif choix == "0":
            vue.afficher_message("Fermeture de l'application.")
            break
        else:
            vue.afficher_message("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
