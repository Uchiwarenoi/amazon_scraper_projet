# Amazon Scraper — Python

## 1. Présentation du projet

Amazon Scraper est une application console développée en Python permettant de rechercher des produits informatiques sur Amazon, de récupérer leurs informations et de les enregistrer dans une base de données locale.

Le projet permet de mettre en pratique le web scraping avec Selenium, la programmation orientée objet, l'architecture MVC, la gestion d'une base SQLite et l'exportation de données au format CSV.

## 2. Fonctionnalités principales

- **Recherche par catégorie :** recherche de produits informatiques à partir des catégories proposées par l'application.
- **Recherche libre :** recherche par nom de produit, marque ou référence.
- **Extraction de données :** récupération du nom, du prix, de l'URL du produit et de l'URL de son image lorsque ces informations sont disponibles.
- **Téléchargement des images :** enregistrement des images récupérées dans le dossier `data/images/`.
- **Gestion des produits :** ajout manuel, consultation, recherche par marque et comptage des produits enregistrés.
- **Stockage local :** conservation des informations et du chemin des images dans une base SQLite.
- **Exportation CSV :** exportation des informations des produits, notamment les URL et les chemins des images.

Le nombre de produits récupérés est limité à 20 par recherche, selon la configuration et les résultats disponibles.

## 3. Technologies utilisées

- **Python :** langage principal.
- **Selenium :** automatisation du navigateur et extraction des données.
- **Google Chrome :** navigateur utilisé pour la recherche.
- **Requests :** téléchargement des images à partir de leurs URL.
- **SQLite :** stockage local des produits.
- **CSV :** exportation des données.
- **Git et GitHub :** gestion des versions et hébergement du code.

## 4. Architecture du projet

Le projet utilise une architecture inspirée du modèle MVC (Model - View - Controller).

```text
amazon_work/
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
│   ├── images/
│   └── produits.db
├── exports/
├── config.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

Cette arborescence représente l'organisation prévue du projet. Les noms des fichiers doivent correspondre à ceux réellement présents dans le dépôt.

- **Model :** représente les produits et gère l'accès à la base de données.
- **View :** affiche les menus et les résultats, et gère l'exportation.
- **Controller :** coordonne les opérations de recherche et d'enregistrement.
- **Scraper :** automatise le navigateur, récupère les informations et télécharge les images.

## 5. Installation et configuration

### Prérequis

- Python installé.
- Google Chrome installé.
- Une connexion Internet.
- Le fichier `requirements.txt`.

### Étape 1 : récupérer le projet

```bash
git clone URL_DU_DEPOT
cd amazon_work
```

Remplace `URL_DU_DEPOT` par l'adresse réelle de ton dépôt GitHub. Si le projet est déjà sur ton ordinateur, ouvre simplement son dossier dans le terminal.

### Étape 2 : créer un environnement virtuel

```bash
python -m venv venv
```

### Étape 3 : activer l'environnement virtuel

Sous Windows avec CMD :

```cmd
venv\Scripts\activate
```

Sous PowerShell :

```powershell
.\venv\Scripts\Activate.ps1
```

### Étape 4 : installer les dépendances

```bash
python -m pip install -r requirements.txt
```

Vérifie que `requirements.txt` contient les bibliothèques réellement utilisées, notamment `selenium` et `requests` si le téléchargement des images utilise Requests.

### Étape 5 : vérifier la configuration

Le fichier `config.py` définit notamment le navigateur, les délais d'attente, le nombre maximal de produits et les chemins de stockage.

Les dossiers `data/`, `data/images/` et `exports/` sont créés automatiquement par la configuration.

## 6. Utilisation de l'application

### Lancer l'application

Depuis la racine du projet, exécute :

```bash
python main.py
```

Le menu principal s'affiche dans la console.

### Effectuer une recherche

1. Choisir la recherche par catégorie ou la recherche libre.
2. Sélectionner une catégorie ou saisir le produit recherché.
3. Laisser Selenium ouvrir les résultats Amazon.
4. Consulter les produits récupérés.
5. Vérifier l'enregistrement des produits et de leurs images.

Les informations récupérées dépendent de la disponibilité des pages et de la structure HTML d'Amazon.

### Consulter les données

Les informations des produits sont stockées dans `data/produits.db`.

Les images téléchargées sont conservées dans `data/images/`. La base de données enregistre leur chemin local dans le champ `image_locale`, ainsi que leur URL dans le champ `image_url`.

### Exporter les données

Utilise l'option d'exportation du menu pour générer un fichier CSV dans le dossier `exports/`.

Le fichier CSV contient les informations exportées par l'application, notamment les URL des images et leurs chemins locaux. Il ne contient pas directement les fichiers image.

Pour transférer le projet avec les images, il faut également copier le dossier `data/images/`.

## 7. Résolution des problèmes courants

| Problème | Solution |
|---|---|
| `ModuleNotFoundError` | Activer l'environnement virtuel et installer les dépendances. |
| Python n'est pas reconnu | Vérifier l'installation de Python et le PATH. |
| Chrome ne démarre pas | Vérifier Chrome et la configuration Selenium. |
| Aucun produit n'est récupéré | Vérifier les sélecteurs et la structure HTML de la page. |
| Une image ne se télécharge pas | Vérifier son URL, la connexion Internet et l'accès au serveur. |
| Amazon affiche un CAPTCHA ou bloque l'accès | Arrêter les tentatives répétées et réessayer ultérieurement si l'accès est autorisé. |
| L'export CSV échoue | Vérifier le chemin de destination et les droits d'écriture. |

## 8. Bonnes pratiques

- Activer l'environnement virtuel avant d'exécuter le programme.
- Utiliser `WebDriverWait` pour attendre les éléments nécessaires.
- Éviter les requêtes excessives.
- Respecter les conditions d'utilisation d'Amazon et les règles applicables à la collecte automatisée.
- Ne pas versionner l'environnement virtuel `venv/` ni les fichiers sensibles.
- Effectuer régulièrement des commits Git.
- Vérifier que le dossier `data/images/` et la base SQLite sont correctement sauvegardés si les données doivent être conservées.
