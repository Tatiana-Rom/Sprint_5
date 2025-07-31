from selenium.webdriver.common.by import By

class ProfilePageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    PROFILE_TAB = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button') and contains(text(), 'Выход')]")
