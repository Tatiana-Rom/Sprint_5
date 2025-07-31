import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_locators import ProfilePageLocators
from data.urls import MAIN

class TestNavigationFromAccount:
    def test_navigate_via_constructor_button(self, logged_in_driver):
        """Переход по кнопке 'Конструктор' из личного кабинета"""
        driver = logged_in_driver
        driver.get(f"{MAIN}/account")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TAB)
        )

        constructor_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Конструктор']"))
        )
        constructor_btn.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{MAIN}/")
        )
        assert driver.current_url.rstrip("/") == MAIN.rstrip("/")

    def test_navigate_via_logo(self, logged_in_driver):
        """Переход по логотипу из личного кабинета"""
        driver = logged_in_driver
        driver.get(f"{MAIN}/account")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TAB)
        )

        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "AppHeader_header__logo__2D0X2"))
        )
        logo.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{MAIN}/")
        )
        assert driver.current_url.rstrip("/") == MAIN.rstrip("/")
