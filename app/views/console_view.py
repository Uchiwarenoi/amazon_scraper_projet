class ConsoleView:
    SOUS_CATEGORIES_TECH = {
        "1": ("Ordinateurs portables", "laptop"),
        "2": ("PC de bureau", "desktop computer"),
        "3": ("Composants informatiques", "computer components CPU GPU RAM SSD"),
        "4": ("Périphériques", "computer monitor keyboard mouse webcam"),
        "5": ("Consoles et jeux vidéo", "video game console gaming accessories"),
        "6": ("Téléphones et tablettes", "smartphone tablet"),
        "7": ("Réseau et connectivité", "router wifi network adapter"),
        "8": ("Stockage et accessoires", "external hard drive USB flash drive computer accessories"),
    }

    def afficher_menu(self):
        print("\n========== AMAZON SCRAPER ==========")
        print("1. Scraper les outils informatiques et technologiques")
        print("2. Scraper une autre catégorie (saisie libre)")
        print("3. Afficher les produits enregistrés")
        print("4. Rechercher les produits enregistrés par marque")
        print("5. Compter les produits enregistrés")
        print("6. Ajouter un produit manuellement")
        print("7. Exporter les produits en CSV")
        print("0. Quitter")
        print("====================================")

    def demander_choix(self):
        return input("Votre choix : ").strip()

    def demander_sous_categorie_tech(self):
        print("\n--- OUTILS INFORMATIQUES ET TECHNOLOGIQUES ---")
        for numero, (nom, _) in self.SOUS_CATEGORIES_TECH.items():
            print(f"{numero}. {nom}")
        print("0. Retour")
        choix = input("Choisissez une sous-catégorie : ").strip()
        if choix == "0":
            return None
        if choix not in self.SOUS_CATEGORIES_TECH:
            print("Sous-catégorie invalide.")
            return None
        return self.SOUS_CATEGORIES_TECH[choix]

    def demander_categorie_libre(self):
        recherche = input("Entrez le nom de l'article à rechercher : ").strip()

        if not recherche:
            print("Le nom de l'article ne peut pas être vide.")
            return None

        return recherche

    def afficher_resultats_scraping(self, produits):
        if not produits:
            print("Aucun résultat à afficher.")
            return
        print(f"\n--- RÉSULTATS ({len(produits)} produits, maximum 20) ---")
        for index, p in enumerate(produits, start=1):
            print(f"{index}. {p['nom']}\n   Prix : {p['prix']}")
            if p.get("url_produit"):
                print(f"   Lien : {p['url_produit']}")
            print("-" * 50)

    def demander_marque(self):
        return input("Entrez la marque à rechercher : ").strip()

    def afficher_produits(self, produits):
        if not produits:
            print("Aucun produit enregistré.")
            return
        for p in produits:
            print("-" * 50)
            print(f"ID : {p[0]}\nNom : {p[1]}\nPrix : {p[2]}\nMarque : {p[4]}\nCatégorie : {p[7]}\nURL : {p[8]}")

    def afficher_message(self, message):
        print(message)

    def demander_produit(self):
        print("\n--- Ajouter un produit ---")
        return {"nom": input("Nom du produit : ").strip(), "prix": input("Prix du produit : ").strip(),
                "description": input("Description : ").strip(), "marque": input("Marque : ").strip(),
                "image_url": input("URL de l'image : ").strip(), "image_locale": "",
                "categorie": input("Catégorie : ").strip(), "url_produit": input("URL du produit : ").strip()}

    def afficher_export(self, chemin):
        print(f"Export réalisé : {chemin}")
