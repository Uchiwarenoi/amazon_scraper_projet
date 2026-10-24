from urllib.parse import quote_plus
from urllib.request import urlopen
from urllib.robotparser import RobotFileParser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from app.scraper_utile.driver import creer_driver, fermer_driver
from config import SITE_AMAZON, ROBOTS_AMAZON, TIMEOUT_ELEMENT, NOMBRE_MAX_PRODUITS

class AmazonScraper:
    def verifier_acces(self, url):
        driver = None
        try:
            driver = creer_driver()
            driver.get(url)
            print("Accès au site réussi.")
            return True
        except Exception as erreur:
            print(f"Impossible d'ouvrir le site : {erreur}")
            return False
        finally:
            if driver is not None:
                fermer_driver(driver)

    def verifier_robots(self, url_page=None):
        try:
            with urlopen(ROBOTS_AMAZON, timeout=10) as reponse:
                contenu = reponse.read().decode("utf-8", errors="replace")
            parser = RobotFileParser()
            parser.parse(contenu.splitlines())
            return parser.can_fetch("*", url_page or SITE_AMAZON)
        except Exception:
            return False

    @staticmethod
    def _texte(element, selecteur):
        for candidat in element.find_elements(By.CSS_SELECTOR, selecteur):
            texte = candidat.text.strip()
            if texte:
                return texte
        return ""

    @staticmethod
    def _prix(element):
        entier = AmazonScraper._texte(element, "span.a-price-whole")
        decimal = AmazonScraper._texte(element, "span.a-price-fraction")
        symbole = AmazonScraper._texte(element, "span.a-price-symbol")
        if entier:
            valeur = entier.replace("\n", "").strip()
            if decimal:
                valeur += decimal.strip()
            return f"{symbole}{valeur}".strip()
        return AmazonScraper._texte(element, "span.a-offscreen") or "Non disponible"

    def rechercher_produit(self, recherche):
        if not recherche.strip():
            print("Veuillez saisir un produit.")
            return False

        terme = quote_plus(recherche)
        url = f"{SITE_AMAZON}/s?k={terme}"

        if not self.verifier_robots(url):
            print("URL non autorisée ou vérification impossible.")
            return False

        driver = None

        try:
            driver = creer_driver()
            driver.get(url)

            WebDriverWait(driver, 15).until(
                lambda d: d.find_element(By.TAG_NAME, "body").text.strip()
            )

            contenu = driver.find_element(
                By.TAG_NAME, "body"
            ).text.lower()

            if (
                    "dogs of amazon" in contenu
                    or "internal error" in contenu
                    or "sorry! something went wrong" in contenu
            ):
                print("Amazon a renvoyé une page d'erreur.")
                print("Aucun produit n'a été récupéré.")
                print("Réessaie plus tard ou vérifie Amazon dans ton navigateur.")
                return False

            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (
                            By.CSS_SELECTOR,
                            "div[data-component-type='s-search-result']"
                        )
                    )
                )
            except TimeoutException:
                print("Aucun résultat de recherche détecté sur la page.")
                return False

            produits = driver.find_elements(
                By.CSS_SELECTOR,
                "div[data-component-type='s-search-result']"
            )

            nombre = 0

            for produit in produits:
                if nombre >= 20:
                    break

                titres = produit.find_elements(
                    By.CSS_SELECTOR, "h2 a span"
                )

                if not titres:
                    continue

                nom = titres[0].text.strip()

                if not nom:
                    continue

                prix_entier = produit.find_elements(
                    By.CSS_SELECTOR, "span.a-price-whole"
                )

                prix_decimal = produit.find_elements(
                    By.CSS_SELECTOR, "span.a-price-fraction"
                )

                prix = "Non disponible"

                if prix_entier:
                    prix = prix_entier[0].text.strip()

                    if prix_decimal:
                        prix += prix_decimal[0].text.strip()

                nombre += 1
                print(f"{nombre}. Produit : {nom}")
                print(f"   Prix : {prix}")
                print("-" * 40)

            if nombre == 0:
                print("Aucun produit exploitable n'a été trouvé.")

            return nombre > 0

        except Exception as erreur:
            print(f"Erreur pendant la recherche : {erreur}")
            return False

        finally:
            if driver is not None:
                fermer_driver(driver)

    def rechercher_produit(self, recherche):
        resultats = self.rechercher_produits(recherche)
        for i, produit in enumerate(resultats, start=1):
            print(f"{i}. {produit['nom']}\n   Prix : {produit['prix']}\n   Lien : {produit['url_produit']}\n{'-' * 50}")
        return bool(resultats)
