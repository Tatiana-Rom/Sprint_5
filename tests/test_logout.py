import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.user import PersonData

class TestLogoutFromAccount:

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Фикстура подготовки: авторизация пользователя"""
        self.driver = driver
        self.base_url = base_url
        
        self.driver.get(f"{base_url}/login")
        email_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
        )
        email_field.send_keys(PersonData.login)
        
        password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")
        password_field.send_keys(PersonData.password)
        
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()
        
      
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )

    def test_logout_via_logout_button(self):
        """Проверка выхода из аккаунта"""
        
        account_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"))
        )
        account_button.click()
        
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Профиль')]"))
        )
        
        logout_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Account_button') and contains(text(), 'Выход')]"))
        )
        logout_button.click()
        

        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/login")
        )
       
        assert WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Войти')]"))
        ), "Кнопка 'Войти' не отображается после выхода"