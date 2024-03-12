import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(request, get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
    url = 'https://exchange.konomik.com/authorization/signup'
    request.cls.driver = driver
    driver.get(url)
