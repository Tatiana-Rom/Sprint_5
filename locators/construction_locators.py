from selenium.webdriver.common.by import By

class ConstructorPageLocators:

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'tab_tab')]")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'tab_tab')]")
    TOPPINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'tab_tab')]")

    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    TOPPINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")

    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")