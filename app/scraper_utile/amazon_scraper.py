import time
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser
from urllib.request import Request, urlopen
import requests
from pathlib import Path
from urllib.parse import urlparse
from config import DOSSIER_IMAGES

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)

from app.scraper_utile.driver import creer_driver, fermer_driver
from config import (
    SITE_AMAZON,
    ROBOTS_AMAZON,
    TIMEOUT_ELEMENT,
    NOMBRE_MAX_PRODUITS
)


CARTE = 'div[data-component-type="s-search-result"]'

MARQUES_CAPTCHA = (
    "captchacharacters",
    "enter the characters you see below",
    "type the characters you see in this image",
)


class AmazonScraper:

    def captcha(self, driver):
        source = driver.page_source.lower()

        return (
            "validatecaptcha" in driver.current_url.lower()
            or any(marque in source for marque in MARQUES_CAPTCHA)
        )

    def gerer_blocage(self, driver):
        for _ in range(4):
            source = driver.page_source.lower()

            if (
                "continue shopping" in source
                and "twotabsearchtextbox" not in source
            ):
                try:
                    driver.find_element(
                        By.XPATH,
                        "//button[contains(., 'Continue shopping')]"
                    ).click()
                    time.sleep(2)
                    continue
                except NoSuchElementException:
                    pass

            if not self.captcha(driver):
                return True

            print("Amazon demande une vérification manuelle.")
            reponse = input(
                "Résous la vérification dans Chrome, puis appuie "
                "sur Entrée (ou q pour annuler) : "
            ).strip().lower()

            if reponse == "q":
                return False

            time.sleep(2)

        return not self.captcha(driver)

    def verifier_robots(self, url):
        try:
            with urlopen(ROBOTS_AMAZON, timeout=10) as reponse:
                contenu = reponse.read().decode(
                    "utf-8", errors="replace"
                )

            parser = RobotFileParser()
            parser.parse(contenu.splitlines())

            return parser.can_fetch("*", url)

        except Exception as erreur:
            print(f"Vérification robots.txt impossible : {erreur}")
            return False

    @staticmethod
    def lire(element, selecteur, attribut="textContent"):
        try:
            valeur = element.find_element(
                By.CSS_SELECTOR, selecteur
            ).get_attribute(attribut)

            return (valeur or "").strip() or None

        except NoSuchElementException:
            return None

    @staticmethod
    def extraire_prix(element):
        return (
            AmazonScraper.lire(
                element,
                '[data-cy="price-recipe"] span.a-price '
                'span.a-offscreen'
            )
            or AmazonScraper.lire(
                element,
                "span.a-price span.a-offscreen"
            )
            or "Non disponible"
        )

    def rechercher_produits(
        self, recherche, categorie=None, limite=20
    ):
        if not recherche or not recherche.strip():
            print("Veuillez saisir un produit.")
            return []

        page_accueil = SITE_AMAZON.rstrip("/") + "/"

        if not self.verifier_robots(page_accueil):
            print(
                "Accès à la page d'accueil non autorisé "
                "ou robots.txt inaccessible."
            )
            return []

        driver = None
        resultats = []
        vus = set()

        try:
            driver = creer_driver()

            # 1. Ouvrir la page d'accueil
            driver.get(page_accueil)

            WebDriverWait(
                driver, TIMEOUT_ELEMENT
            ).until(
                EC.presence_of_element_located(
                    (By.TAG_NAME, "body")
                )
            )

            if not self.gerer_blocage(driver):
                print("Recherche annulée.")
                return []

            # 2. Saisir la recherche dans la barre Amazon
            attente = WebDriverWait(driver, TIMEOUT_ELEMENT)

            barre = attente.until(
                EC.element_to_be_clickable(
                    (By.ID, "twotabsearchtextbox")
                )
            )

            barre.clear()
            barre.send_keys(recherche.strip())
            barre.send_keys(Keys.ENTER)

            # 3. Vérifier la page de résultats
            if not self.gerer_blocage(driver):
                print("Recherche annulée.")
                return []

            attente.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, CARTE)
                )
            )

            maximum = min(
                max(0, limite),
                NOMBRE_MAX_PRODUITS
            )

            # 4. Extraire les produits
            produits = driver.find_elements(
                By.CSS_SELECTOR, CARTE
            )

            for produit in produits:
                if len(resultats) >= maximum:
                    break

                asin = (
                    produit.get_attribute("data-asin") or ""
                ).strip()

                titre = (
                    self.lire(
                        produit, '[data-cy="title-recipe"] h2'
                    )
                    or self.lire(produit, "h2")
                )

                if not titre or (asin and asin in vus):
                    continue

                if asin:
                    vus.add(asin)

                lien = self.lire(
                    produit, "h2 a", "href"
                )

                if not lien and asin:
                    lien = urljoin(page_accueil, f"dp/{asin}")

                images = produit.find_elements(
                    By.CSS_SELECTOR, "img.s-image"
                )

                image = (
                    images[0].get_attribute("src") or ""
                    if images else ""
                )

                resultats.append({
                    "nom": titre,
                    "prix": self.extraire_prix(produit),
                    "description": "",
                    "marque": "Inconnue",
                    "image_url": image,
                    "image_locale": "",
                    "categorie": categorie or "Autres",
                    "url_produit": lien or ""
                })

            print(
                f"{len(resultats)} produit(s) récupéré(s)."
            )

            return resultats

        except TimeoutException:
            print(
                "Délai dépassé : barre de recherche ou "
                "résultats introuvables."
            )
            print("URL actuelle :", driver.current_url if driver else "")
            print("Titre :", driver.title if driver else "")
            return []

        except Exception as erreur:
            print(f"Erreur pendant la recherche : {erreur}")
            return []

        finally:
            if driver is not None:
                fermer_driver(driver)

    def rechercher_produit(self, recherche):
        resultats = self.rechercher_produits(recherche)

        for numero, produit in enumerate(resultats, start=1):
            print(
                f"\n{numero}. {produit['nom']}\n"
                f"Prix : {produit['prix']}\n"
                f"Lien : {produit['url_produit']}\n"
                f"{'-' * 40}"
            )

        return bool(resultats)

    def telecharger_image(self, image_url):
        if not image_url:
            return None

        try:
            requete = Request(
                image_url,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            with urlopen(requete, timeout=10) as reponse:
                return reponse.read()

        except Exception:
            return None

    def enregistrer_image(self, image_url, nom_fichier):
        if not image_url:
            return ""

        try:
            reponse = requests.get(
                image_url,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=15
            )
            reponse.raise_for_status()

            extension = Path(
                urlparse(image_url).path
            ).suffix.lower()

            if extension not in [".jpg", ".jpeg", ".png", ".webp"]:
                extension = ".jpg"

            chemin = DOSSIER_IMAGES / f"{nom_fichier}{extension}"
            chemin.write_bytes(reponse.content)

            return str(chemin)

        except requests.RequestException:
            return ""