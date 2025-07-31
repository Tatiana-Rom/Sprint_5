import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.user import PersonData


def perform_login(driver, email, password):
    """Общая функция логина для всех тестов"""
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
    )

    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='email' or @name='email' or @name='name']"))
    )
    email_field.clear()
    email_field.send_keys(email)

    password_field = driver.find_element(
        By.XPATH, "//input[@type='password' or @name='password']"
    )
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()


def test_login_from_main_page(driver, base_url):
    """Тест входа по кнопке 'Войти в аккаунт' на главной"""
    driver.get(base_url)
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
    ).click()
    
    perform_login(driver, PersonData.login, PersonData.password)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )


def test_login_from_account_button(driver, base_url):
    """Тест входа через кнопку 'Личный кабинет'"""
    driver.get(base_url)
    

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
    ).click()
    
    perform_login(driver, PersonData.login, PersonData.password)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )

def test_login_from_registration_form(driver, base_url):
    """Тест входа через форму регистрации"""
    driver.get(f"{base_url}/register")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
    ).click()
    
    perform_login(driver, PersonData.login, PersonData.password)


    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )


def test_login_from_password_recovery(driver, base_url):
    """Тест входа через форму восстановления пароля"""
    driver.get(f"{base_url}/forgot-password")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
    ).click()
    
    perform_login(driver, PersonData.login, PersonData.password)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )