from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def __get_selenium_by(self, find_by: str) -> dict:
        """Список локаторов в котором ключ это - строка локатор списка, значения связанны значениями поиска"""
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def find_element(self, locator: str, locator_name: str = None, time=15) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      locator_name)

    def shadow_root(self, locator_host: str, locator_content: str, locator_name: str = None, time=15) -> WebElement:
        shadow_host = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locator_host)),
            locator_name)
        shadow_root = shadow_host.shadow_root
        shadow_content = shadow_root.find_element(By.CSS_SELECTOR, locator_content)
        return shadow_content
