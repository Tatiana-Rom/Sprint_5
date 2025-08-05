import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import MAIN, LOGIN
from locators.login_locators import LoginPageLocators
from locators.profile_locators import ProfilePageLocators

class TestPersonalAccount:
    def test_personal_account_click(self, driver):
        """Проверка перехода в личный кабинет для неавторизованного пользователя"""

        driver.get(MAIN)

        account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        expected_url = LOGIN
        assert driver.current_url == expected_url, \
            f"Ожидался переход на {expected_url}, но открыт {driver.current_url}"

        login_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.HEADER)
        )
        assert login_title.is_displayed(), "Заголовок 'Вход' не отображается"