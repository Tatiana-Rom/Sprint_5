import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPersonalAccount:
    def test_personal_account_click(self, driver, base_url):
        """Проверка перехода в личный кабинет для неавторизованного пользователя"""
   
        driver.get(base_url)
        
        account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/account']"))
        )
        account_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        expected_url = f"{base_url}/login"
        assert driver.current_url == expected_url, \
            f"Ожидался переход на {expected_url}, но открыт {driver.current_url}"
        
        login_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        assert login_title.is_displayed(), "Заголовок 'Вход' не отображается"