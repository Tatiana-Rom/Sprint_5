from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginPageLocators

class LoginHelper:
    @staticmethod
    def perform_login(driver, email, password):
        """Выполняет ввод данных и вход в систему"""
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
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
        )