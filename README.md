# Amazon Scraper

Application console Python organisée en MVC avec Selenium et SQLite.

## Fonctionnalités
- Scraping d'outils informatiques et technologiques par sous-catégorie.
- Recherche libre d'une autre catégorie ou d'un produit.
- Maximum de 20 résultats par recherche.
- Enregistrement SQLite, consultation, recherche par marque et export CSV.

## Installation (Windows)
Dans le terminal ouvert à la racine du projet :

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Google Chrome doit être installé. Les versions récentes de Selenium peuvent gérer le pilote Chrome avec Selenium Manager.

Le site peut modifier son HTML, afficher des vérifications ou refuser l'accès. Le programme ne contourne pas ces protections. La vérification robots.txt reste silencieuse dans la console. Respectez les conditions d'utilisation du site.
