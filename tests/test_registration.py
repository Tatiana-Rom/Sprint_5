import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import MAIN, REGISTER, FORGOT_PASSWORD
from data.user import PersonData
from locators.profile_locators import ProfilePageLocators
from locators.login_locators import LoginPageLocators
from helpers.auth import LoginHelper

class TestLogin:
    """Тесты авторизации пользователя"""

    def test_login_from_main_page(self, driver):
        driver.get(MAIN)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_MAIN_PAGE_BUTTON)
        ).click()

        LoginHelper.perform_login(driver, PersonData.login, PersonData.password)
        assert driver.current_url == MAIN

    def test_login_from_account_button(self, driver):
        driver.get(MAIN)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.ACCOUNT_BUTTON)
        ).click()

        LoginHelper.perform_login(driver, PersonData.login, PersonData.password)
        assert driver.current_url == MAIN

    def test_login_from_registration_form(self, driver):
        driver.get(REGISTER)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_REGISTER_PAGE_LINK)
        ).click()

        LoginHelper.perform_login(driver, PersonData.login, PersonData.password)
        assert driver.current_url == MAIN

    def test_login_from_password_recovery(self, driver):
        driver.get(FORGOT_PASSWORD)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_FORGOT_PASSWORD_LINK)
        ).click()

        LoginHelper.perform_login(driver, PersonData.login, PersonData.password)
        assert driver.current_url == MAIN