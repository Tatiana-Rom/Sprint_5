import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import MAIN
from locators.login_locators import LoginPageLocators
from helpers.auth import perform_login

class TestLogin:
    def test_login_from_main_page_button(self, driver, login):
        driver.get(MAIN)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_MAIN_PAGE_BUTTON)
        ).click()

        perform_login(driver, login["email"], login["password"], MAIN)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
        )

    def test_login_from_account_button(self, driver, login):
        driver.get(MAIN)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_ACCOUNT_BUTTON)
        ).click()

        perform_login(driver, login["email"], login["password"], MAIN)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
        )

    def test_login_from_registration_form(self, driver, login):
        driver.get(f"{MAIN}/register")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_REGISTER_PAGE_LINK)
        ).click()

        perform_login(driver, login["email"], login["password"], MAIN)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
        )

    def test_login_from_forgot_password_form(self, driver, login):
        driver.get(f"{MAIN}/forgot-password")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_FORGOT_PASSWORD_LINK)
        ).click()

        perform_login(driver, login["email"], login["password"], MAIN)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
        )