import sqlite3
from config import BASE_DE_DONNEES

class Depot:
    def __init__(self, chemin=BASE_DE_DONNEES):
        self.chemin = chemin
        self.creer_table()

    def connecter(self):
        return sqlite3.connect(self.chemin)

    def creer_table(self):
        with self.connecter() as connexion:
            connexion.execute("""CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL, prix REAL,
                description TEXT, marque TEXT, image_url TEXT, image_locale TEXT,
                categorie TEXT, url_produit TEXT UNIQUE)""")

    def ajouter_produit(self, produit):
        with self.connecter() as connexion:
            curseur = connexion.execute("""INSERT OR IGNORE INTO produits
                (nom, prix, description, marque, image_url, image_locale, categorie, url_produit)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (
                produit.nom, produit.prix, produit.description, produit.marque,
                produit.image_url, produit.image_locale, produit.categorie, produit.url_produit or None))
            return curseur.rowcount > 0

    def obtenir_tous(self):
        with self.connecter() as connexion:
            return connexion.execute("""SELECT id, nom, prix, description, marque,
                image_url, image_locale, categorie, url_produit FROM produits ORDER BY id DESC""").fetchall()

    def rechercher_par_marque(self, marque):
        with self.connecter() as connexion:
            return connexion.execute("""SELECT id, nom, prix, description, marque,
                image_url, image_locale, categorie, url_produit FROM produits
                WHERE marque LIKE ? ORDER BY nom""", (f"%{marque}%",)).fetchall()

    def compter_produits(self):
        with self.connecter() as connexion:
            return connexion.execute("SELECT COUNT(*) FROM produits").fetchone()[0]
