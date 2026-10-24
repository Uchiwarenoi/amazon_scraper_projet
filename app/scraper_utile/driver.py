
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import TIMEOUT_CHARGEMENT


def creer_driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.set_page_load_timeout(TIMEOUT_CHARGEMENT)
    driver.set_script_timeout(TIMEOUT_CHARGEMENT)

    return driver


def fermer_driver(driver):
    if driver is not None:
        driver.quit()
