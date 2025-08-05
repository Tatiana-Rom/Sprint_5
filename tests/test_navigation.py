import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_locators import ProfilePageLocators
from locators.construction_locators import ConstructorPageLocators
from locators.login_locators import LoginPageLocators
from data.urls import MAIN, ACCOUNT


class TestNavigationFromAccount:
    def test_navigate_via_constructor_button(self, logged_in_driver):
        """Переход по кнопке 'Конструктор' из личного кабинета"""
        driver = logged_in_driver

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.ACCOUNT_BUTTON)
        )

        constructor_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.LINK_CONSTRUCT)
        )
        constructor_btn.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(MAIN)
        )
        assert driver.current_url == MAIN

    def test_navigate_via_logo(self, logged_in_driver):
        """Переход по логотипу из личного кабинета"""
        driver = logged_in_driver
        driver.get(MAIN)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.ACCOUNT_BUTTON)
        )

        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGO)
        )
        logo.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(MAIN)
        )
        assert driver.current_url == MAIN