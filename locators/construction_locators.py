from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TOPPINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.CSS_SELECTOR, ".tab_tab__1SPyG.tab_tab_type_current__2BEPc")