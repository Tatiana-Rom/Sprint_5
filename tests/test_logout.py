import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_locators import ProfilePageLocators
from locators.login_locators import LoginPageLocators

class TestLogout:
    """Проверка выхода из аккаунта через личный кабинет"""
    def test_logout_via_account(self, logged_in_driver):
        driver = logged_in_driver

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.ACCOUNT_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()

        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed(), "После выхода не видно кнопку входа"
        assert "/login" in driver.current_url.lower(), "После выхода должен быть редирект на страницу логина"
