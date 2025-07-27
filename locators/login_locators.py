from selenium.webdriver.common.by import By

class LoginLocators:

    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    

    LOGIN_LINK_REGISTER = (By.XPATH, "//a[text()='Войти']")  
    LOGIN_LINK_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Войти']")  