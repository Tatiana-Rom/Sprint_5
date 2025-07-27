import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.user import ValidData

email = ValidData.login
password = ValidData.password

def test_successful_registration(driver, base_url):
    driver.get(base_url)

    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))

    name = ValidData.user_name
    email = ValidData.login
    password = ValidData.password

    driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys(name)
    driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(email)
    driver.find_element(By.XPATH, "//fieldset[3]//input").send_keys(password)

    assert "@" in email and "." in email.split("@")[1], "Некорректный email"
    assert len(password) >= 6, "Пароль слишком короткий"

    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data", "last_user.txt")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"{email},{password}")

def test_registration_with_short_password(driver, base_url):
    driver.get(base_url)

    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))

    name = ValidData.user_name
    email = ValidData.login
    short_password = "12345"

    driver.find_element(By.XPATH, "//fieldset[1]//input").send_keys(name)
    driver.find_element(By.XPATH, "//fieldset[2]//input").send_keys(email)
    driver.find_element(By.XPATH, "//fieldset[3]//input").send_keys(short_password)

    assert len(short_password) < 6, "Тест должен использовать пароль < 6 символов"

    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()


    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"))
    )
    assert error.is_displayed(), "Ожидалась ошибка о некорректном пароле"