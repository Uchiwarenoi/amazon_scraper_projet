
from selenium.webdriver.common.by import By


def obtenir_texte(element, selecteur, valeur_defaut="Non disponible"):
    try:
        texte = element.find_element(By.CSS_SELECTOR, selecteur).text.strip()

        if texte:
            return texte

        return valeur_defaut

    except Exception:
        return valeur_defaut


def obtenir_attribut(element, selecteur, attribut, valeur_defaut=""):
    try:
        resultat = element.find_element(
            By.CSS_SELECTOR, selecteur
        ).get_attribute(attribut)

        return resultat if resultat else valeur_defaut

    except Exception:
        return valeur_defaut
