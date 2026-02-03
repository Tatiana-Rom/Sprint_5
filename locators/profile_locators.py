from selenium.webdriver.common.by import By

class ProfilePageLocators:
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
    PROFILE_TAB = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button') and normalize-space()='Выход']")
