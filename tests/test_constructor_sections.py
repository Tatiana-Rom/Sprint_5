import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import MAIN
from locators.construction_locators import ConstructorPageLocators

@pytest.mark.parametrize("tab_locator, expected_text", [
    (ConstructorPageLocators.BUNS_TAB, "Булки"),
    (ConstructorPageLocators.SAUCES_TAB, "Соусы"),
    (ConstructorPageLocators.TOPPINGS_TAB, "Начинки"),
])
def test_switch_tabs(driver, tab_locator, expected_text):
    driver.get(MAIN)
    active_tab_text = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
    ).text

    if active_tab_text != expected_text:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(tab_locator)
        ).click()

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(ConstructorPageLocators.ACTIVE_TAB, expected_text)
    )
    active_tab = driver.find_element(*ConstructorPageLocators.ACTIVE_TAB)
    assert active_tab.text == expected_text
