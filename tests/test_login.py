import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import MAIN, REGISTER, FORGOT_PASSWORD
from locators.registration_locators import RegistrationPageLocators
from locators.profile_locators import ProfilePageLocators
from locators.login_locators import LoginPageLocators
from helpers.auth import LoginHelper


class TestLogin:
    """Тесты авторизации пользователя"""

    def test_login_from_main_page_button(self, driver, login):
        """Тест входа через кнопку на главной странице"""
        driver.get(MAIN)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_MAIN_PAGE_BUTTON)
        ).click()

        LoginHelper.perform_login(driver, login["email"], login["password"])


        assert MAIN == driver.current_url

    def test_login_from_personal_account_button(self, driver, login):
        """Тест входа через кнопку личного кабинета"""
        driver.get(MAIN)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.ACCOUNT_BUTTON)
        ).click()

        LoginHelper.perform_login(driver, login["email"], login["password"])

        assert MAIN == driver.current_url

    def test_login_from_registration_form(self, driver, login):
        """Тест входа через форму регистрации"""
        driver.get(REGISTER)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        ).click()

        LoginHelper.perform_login(driver, login["email"], login["password"])

        assert MAIN == driver.current_url

    def test_login_from_forgot_password_form(self, driver, login):
        """Тест входа через форму восстановления пароля"""
        driver.get(FORGOT_PASSWORD)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_FORGOT_PASSWORD_LINK)
        ).click()

        LoginHelper.perform_login(driver, login["email"], login["password"])

        assert MAIN == driver.current_url
