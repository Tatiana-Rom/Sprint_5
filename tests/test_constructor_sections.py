import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.construction_locators import ConstructorPageLocators

class TestConstructorNavigation:
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.driver.get(base_url)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.BUNS_SECTION)
        )

    @pytest.mark.parametrize("section,locator,expected_text", [
        ("Булки", ConstructorPageLocators.BUNS_SECTION, "Булки"),
        ("Соусы", ConstructorPageLocators.SAUCES_SECTION, "Соусы"),
        ("Начинки", ConstructorPageLocators.TOPPINGS_SECTION, "Начинки")
    ])
    def test_section_navigation(self, section, locator, expected_text):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        
        self.driver.execute_script("arguments[0].click();", element)
        
        active_tab = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert expected_text in active_tab.text