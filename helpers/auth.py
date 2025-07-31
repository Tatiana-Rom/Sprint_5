from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.login_locators import LoginPageLocators

def perform_login(driver, email, password, base_url):
    """Общая функция логина"""
    driver.get(f"{base_url}/login")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.HEADER)
    )

    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)
    )
    email_field.clear()
    email_field.send_keys(email)

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD)
    )
    password_field.clear()
    password_field.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    )
    login_button.click()

    WebDriverWait(driver, 10).until(
        lambda d: "/login" not in d.current_url
    )

def logout(driver):
    """Выход из аккаунта"""

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Профиль']"))
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'Account_button') and contains(text(), 'Выход')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

