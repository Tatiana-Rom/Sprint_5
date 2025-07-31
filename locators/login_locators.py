from selenium.webdriver.common.by import By

class LoginPageLocators:
    HEADER = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_FIELD = (By.XPATH, "//input[@type='email' or @name='email' or @name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password' or @name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

    LOGIN_FROM_MAIN_PAGE_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGIN_FROM_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_FROM_REGISTER_PAGE_LINK = (By.XPATH, "//a[text()='Войти']")
    LOGIN_FROM_FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Войти']")