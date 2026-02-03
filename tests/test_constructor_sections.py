import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.construction_locators import ConstructorPageLocators
from data.urls import MAIN


class TestConstructorTabs:
    """Тесты навигации между разделами конструктора"""

    def test_switch_tab_sauces_to_tab_bread_current(self, driver):
        """Проверка переключения с Соусов на Булки"""
        driver.get(MAIN)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.CURRENT_TAB, "Соусы")
        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.BUNS_TAB)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.CURRENT_TAB, "Булки")
        )

        current_tab = driver.find_element(*ConstructorPageLocators.CURRENT_TAB)
        assert current_tab.text == "Булки", f"Ожидалось 'Булки', но активна '{current_tab.text}'"

    def test_switch_tab_bread_to_tab_sauces_current(self, driver):
        """Проверка переключения с Булок на Соусы"""
        driver.get(MAIN)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.CURRENT_TAB, "Соусы")
        )

        current_tab = driver.find_element(*ConstructorPageLocators.CURRENT_TAB)
        assert current_tab.text == "Соусы", f"Ожидалось 'Соусы', но активна '{current_tab.text}'"

    def test_switch_tab_bread_to_tab_toppings_current(self, driver):
        """Проверка переключения с Булок на Начинки"""
        driver.get(MAIN)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.TOPPINGS_TAB)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(ConstructorPageLocators.CURRENT_TAB, "Начинки")
        )

        current_tab = driver.find_element(*ConstructorPageLocators.CURRENT_TAB)
        assert current_tab.text == "Начинки", f"Ожидалось 'Начинки', но активна '{current_tab.text}'"
