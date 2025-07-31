import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_locators import RegistrationLocators
from data.user import ValidData
from data.urls import MAIN

class TestRegistration:
    def test_successful_registration(self, driver):
        """Успешная регистрация с валидными данными"""
        driver.get(MAIN)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.REGISTRATION_TITLE)
        )

        name = ValidData.user_name
        email = ValidData.login
        password = ValidData.password

        assert "@" in email and "." in email.split("@")[-1], "Некорректный email"
        assert len(password) >= 6, "Пароль слишком короткий"

        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )

    def test_registration_with_short_password(self, driver):
        """Регистрация с коротким паролем — ожидается ошибка"""
        driver.get(MAIN)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.REGISTRATION_TITLE)
        )

        name = ValidData.user_name
        email = ValidData.login
        short_password = "12345"

        assert len(short_password) < 6, "Тест должен использовать слишком короткий пароль"

        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.INCORRECT_PASSWORD_ERROR)
        )
        assert error.is_displayed(), "Ожидалась ошибка о некорректном пароле"