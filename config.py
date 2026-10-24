from pathlib import Path
RACINE = Path(__file__).resolve().parent
DOSSIER_DATA = RACINE / "data"
DOSSIER_EXPORTS = RACINE / "exports"
BASE_DE_DONNEES = DOSSIER_DATA / "produits.db"
NAVIGATEUR = "chrome"
TIMEOUT_CHARGEMENT = 25
TIMEOUT_ELEMENT = 15
NOMBRE_MAX_PRODUITS = 20
SITE_AMAZON = "https://www.amazon.com"
ROBOTS_AMAZON = f"{SITE_AMAZON}/robots.txt"
URL_RECHERCHE_AMAZON = f"{SITE_AMAZON}/s?k="
for dossier in (DOSSIER_DATA, DOSSIER_EXPORTS):
    dossier.mkdir(parents=True, exist_ok=True)
