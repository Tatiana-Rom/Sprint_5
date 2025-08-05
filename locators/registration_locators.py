from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    LOGIN_HEADER = (By.XPATH, "//h2[normalize-space()='Вход']")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    REGISTRATION_HEADER = (By.XPATH, "//h2[normalize-space()='Регистрация']")

    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")

    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(normalize-space(), 'Некорректный пароль')]")