import logging
import time
import warnings

from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By

from . import get_chrome_browser

URL = "https://videoferroni-0.lab.iorestoacasa.work"

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", category=UserWarning)

def run(room, y4m, lifetime=360, headless=1, **kwargs):
    url = kwargs.get('url') or URL

    browser = get_chrome_browser(
        y4m=y4m,
        headless=headless
    )

    browser.get(f"{url}/{room}")

    # Entra nella stanza
    browser.find_element(
        By.XPATH,
        '/html/body/div[2]/div[3]/div/div[2]/div/button'
    ).click()

    time.sleep(lifetime)

    # Esce dalla stanza
    try:
        browser.find_element(
            By.XPATH,
            '/html/body/div/div/header/div/button'
        ).click()
    except Exception as e:
        logger.warning(f"Exit button not found: {e}")

    # Chiude browser
    try:
        browser.close()
    except NoSuchWindowException:
        logger.warning("Browser already closed.")

    logger.info("Drone say goodbye ... Destroyed.")

