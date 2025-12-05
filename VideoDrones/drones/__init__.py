import logging
import os
import warnings
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from videodrone.utils import get_random_y4m

DRIVER_PATH = os.environ.get(
    'VIDEODRONE_DRIVER',
    os.path.join("drivers", "chromedriver")
)

def get_chrome_browser(y4m=None, headless=True):
    y4m_file = get_random_y4m(path=y4m)

    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument('--headless=new')
        # headless=new = richiesto da Chrome 109+;
        # funziona anche su versioni vecchie, fallback automatico

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--use-fake-device-for-media-stream')
    options.add_argument('--use-fake-ui-for-media-stream')
    options.add_argument(f'--use-file-for-fake-video-capture={y4m_file}')
    options.add_argument('--disable-gpu')

    # Creazione Service moderna
    service = Service(DRIVER_PATH)

    browser = webdriver.Chrome(
        service=service,
        options=options
    )

    return browser


def build_drone_name(**kwargs):
    num = kwargs.get('id', random.randrange(1000))
    suffix = kwargs.get('suffix')
    if suffix:
        return f'videodrone-{suffix}-{num}'
    return f'videodrone-{num}'


