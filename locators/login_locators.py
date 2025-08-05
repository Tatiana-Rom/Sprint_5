from selenium.webdriver.common.by import By

class LoginPageLocators:
    HEADER = (By.XPATH, "//h2[normalize-space()='Вход']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email'], input[name='email'], input[name='name']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password'], input[name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
    LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")

    LOGIN_FROM_MAIN_PAGE_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")
    LOGIN_FROM_ACCOUNT_BUTTON = (By.XPATH, "//a[@href = '/account']")
    LOGIN_FROM_REGISTER_PAGE_LINK = (By.XPATH, "//a[normalize-space()='Войти']")
    LOGIN_FROM_FORGOT_PASSWORD_LINK = (By.XPATH, "//a[normalize-space()='Войти']")