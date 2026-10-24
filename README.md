# Amazon Scraper — Python

## 1. Présentation du projet

Amazon Scraper est une application console développée en Python permettant de rechercher des produits informatiques sur Amazon, de récupérer leurs informations et de les enregistrer dans une base de données locale.

Le projet a pour objectif de mettre en pratique le web scraping, la programmation orientée objet, l'architecture MVC et la gestion des données.

## 2. Fonctionnalités principales

L'application propose les fonctionnalités suivantes :

- **Recherche par catégorie :** ordinateurs portables, ordinateurs de bureau, composants informatiques, périphériques, consoles, smartphones, équipements réseau et accessoires.
- **Recherche libre :** saisie directe du nom d'un produit, d'une marque ou d'une référence.
- **Extraction de données :** récupération du nom, du prix et de l'image du produit lorsque ces informations sont disponibles.
- **Gestion des produits :** enregistrement dans SQLite, consultation, recherche par marque, comptage et ajout manuel.
- **Exportation CSV :** sauvegarde des données dans un fichier exploitable avec Excel ou d'autres tableurs.

Le nombre de résultats est limité à 20 produits par recherche, selon les possibilités de la page consultée.

## 3. Technologies et architecture

### Technologies utilisées

- **Python :** langage principal.
- **Selenium :** automatisation du navigateur.
- **Google Chrome :** navigateur utilisé pour les recherches.
- **SQLite :** base de données locale.
- **CSV :** exportation des données.
- **Git et GitHub :** gestion des versions et hébergement du code.

### Architecture du projet

Le projet suit une organisation inspirée du modèle MVC (Model - View - Controller).

```text
amazon_scraper/
├── app/
│   ├── controllers/
│   │   └── scraping_controller.py
│   ├── models/
│   │   ├── depot.py
│   │   └── produit.py
│   ├── scraper_utile/
│   │   ├── driver.py
│   │   └── amazon_scraper.py
│   └── views/
│       ├── console_view.py
│       └── export_view.py
├── data/
├── exports/
├── config.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

Cette arborescence est indicative et doit être adaptée à la structure réelle du projet.

- **Model :** gestion des produits et accès à la base de données.
- **View :** affichage des menus et des résultats.
- **Controller :** coordination entre les différentes parties de l'application.
- **Scraper :** automatisation du navigateur et extraction des informations.

## 4. Installation et configuration

### Prérequis

Avant d'utiliser l'application, il faut disposer de :

- Python installé sur l'ordinateur.
- Google Chrome installé.
- Une connexion Internet.
- Le fichier `requirements.txt` présent à la racine du projet.

### Étape 1 : Cloner le projet

Cloner le repository GitHub :

```bash
git clone https://github.com/TON-USERNAME/amazon_scraper_projet.git
```

Entrer dans le dossier du projet :

```bash
cd amazon_scraper_projet
```

Remplacer `TON-USERNAME` par le nom d'utilisateur GitHub correspondant au repository.

Si le projet est déjà présent sur l'ordinateur, ouvrir directement son dossier dans le terminal.

### Étape 2 : Créer l'environnement virtuel

À la racine du projet, exécuter :

```bash
python -m venv venv
```

Cette commande crée un environnement virtuel nommé `venv`, qui permet d'isoler les bibliothèques utilisées par le projet.

### Étape 3 : Activer l'environnement virtuel

Sous Windows, dans l'invite de commandes (CMD) :

```cmd
venv\Scripts\activate
```

Dans PowerShell :

```powershell
.\venv\Scripts\Activate.ps1
```

Lorsque l'environnement est activé, le préfixe `(venv)` apparaît généralement au début de la ligne du terminal.

### Étape 4 : Installer les dépendances

Avec l'environnement virtuel activé, exécuter :

```bash
python -m pip install -r requirements.txt
```

Cette commande installe les bibliothèques nécessaires au fonctionnement de l'application.

### Étape 5 : Vérifier la configuration

Avant de lancer l'application, vérifier que :

- Les dépendances sont correctement installées.
- Google Chrome est installé et accessible.
- Selenium est correctement configuré.
- Les chemins de stockage de la base de données et des fichiers exportés sont valides.

## 5. Utilisation de l'application console

### Étape 1 : Lancer l'application

Depuis la racine du projet, avec l'environnement virtuel activé, exécuter :

```bash
python main.py
```

Le menu principal s'affiche dans la console.

### Étape 2 : Choisir une fonctionnalité

Lire les options proposées par le menu, puis saisir le numéro correspondant à l'action souhaitée.

Les fonctionnalités prévues sont les suivantes :

- **Recherche par catégorie :** choisir une catégorie de produits informatiques et lancer la recherche.
- **Recherche libre :** saisir directement le nom du produit à rechercher.
- **Consultation des produits :** afficher les produits enregistrés dans la base de données.
- **Recherche par marque :** retrouver les produits correspondant à une marque.
- **Comptage des produits :** afficher le nombre de produits enregistrés.
- **Ajout manuel :** saisir les informations d'un produit pour l'enregistrer.
- **Exportation CSV :** enregistrer les données dans un fichier CSV.
- **Quitter :** fermer l'application.

Les numéros exacts dépendent du menu implémenté dans le code.

### Étape 3 : Effectuer une recherche

Pour rechercher un produit :

1. Sélectionner la recherche par catégorie ou la recherche libre.
2. Choisir une catégorie ou saisir le nom du produit souhaité.
3. Laisser Selenium ouvrir la page de résultats.
4. Consulter les produits récupérés.
5. Enregistrer les résultats dans la base de données si cette opération est proposée par l'application.

La récupération des informations dépend de la disponibilité des pages et de la structure HTML utilisée par Amazon.

### Étape 4 : Consulter et exporter les données

Les produits enregistrés sont conservés dans la base de données SQLite.

Pour exporter les données, sélectionner l'option correspondante dans le menu. Le fichier CSV est généré dans le dossier d'exportation configuré par le projet, généralement `exports/`.

Le fichier peut ensuite être ouvert avec Microsoft Excel, LibreOffice Calc ou un autre tableur compatible.

### Étape 5 : Résoudre les problèmes courants

| Problème | Solution |
|---|---|
| `ModuleNotFoundError` | Activer l'environnement virtuel et installer les dépendances. |
| `python` n'est pas reconnu | Vérifier l'installation de Python et sa configuration dans le PATH. |
| Chrome ne démarre pas | Vérifier l'installation de Chrome et la configuration de Selenium. |
| Amazon affiche une erreur | Réessayer ultérieurement et vérifier les conditions d'accès au site. |
| Aucun produit n'est récupéré | Vérifier les sélecteurs HTML et la structure de la page consultée. |
| L'exportation échoue | Vérifier le chemin du fichier et les droits d'écriture. |

### Bonnes pratiques

- Activer l'environnement virtuel avant chaque utilisation.
- Utiliser `WebDriverWait` pour attendre les éléments nécessaires au lieu de multiplier les pauses fixes.
- Éviter les requêtes excessives.
- Respecter les conditions d'utilisation d'Amazon et les règles applicables à la collecte automatisée des données.
- Ne pas versionner l'environnement virtuel `venv/` dans Git.
- Effectuer régulièrement des commits pour conserver un historique des modifications.


