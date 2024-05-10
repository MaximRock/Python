import pytest
from links.links import Links
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import allure
import os
from allure_commons.types import AttachmentType
from datetime import datetime


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument("chrome")
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    return options


@pytest.fixture
def get_webdriver(request, get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
    url = f'{Links.AUTH_SIGNUP}'
    request.cls.driver = driver
    driver.get(url)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()

