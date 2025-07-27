import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.user import PersonData

class TestNavigationFromPersonalAccount:
    def login(self, driver, base_url):
        """Метод для авторизации пользователя"""
        driver.get(f"{base_url}/login")

        email_field = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='name' or @name='email']"))
        )
        email_field.clear()
        email_field.send_keys(PersonData.login)

        password_field = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))
        )
        password_field.clear()
        password_field.send_keys(PersonData.password)

        login_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]"))
        )
        login_button.click()

        WebDriverWait(driver, 15).until(
            lambda d: d.current_url != f"{base_url}/login"
        )

    def test_navigate_via_constructor_button(self, driver, base_url):
        """Проверка перехода по кнопке 'Конструктор'"""
        self.login(driver, base_url)

        driver.get(f"{base_url}/account")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Профиль')]"))
        )

        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Конструктор']"))
        )
        constructor_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{base_url}/")
        )
        assert driver.current_url == f"{base_url}/"

    def test_navigate_via_logo(self, driver, base_url):
        """Проверка перехода по логотипу"""
        self.login(driver, base_url)

        driver.get(f"{base_url}/account")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Профиль')]"))
        )

        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "AppHeader_header__logo__2D0X2"))
        )
        logo.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{base_url}/")
        )
        assert driver.current_url == f"{base_url}/"
