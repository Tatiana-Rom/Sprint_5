from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_locators import ProfilePageLocators
from locators.login_locators import LoginPageLocators

class TestLogout:
    def test_logout_via_account(self, logged_in_driver):
        """Проверка выхода из аккаунта через личный кабинет"""
        driver = logged_in_driver

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )

        assert not driver.current_url.endswith("/account"), \
            "После выхода не должно быть доступа к личному кабинету"
