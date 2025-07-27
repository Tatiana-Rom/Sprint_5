from selenium.webdriver.common.by import By

class RegistrationLocators:
    REGISTRATION_TITLE = (By.XPATH, "//h2[text()='Регистрация']")  
    
    NAME_INPUT = (By.XPATH, "//fieldset[1]//input")  
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]//input")  
    PASSWORD_INPUT = (By.XPATH, "//fieldset[3]//input")  
    
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  
    
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")  
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")