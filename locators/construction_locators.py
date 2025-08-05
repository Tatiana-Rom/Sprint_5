from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[normalize-space()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[normalize-space()='Соусы']")
    TOPPINGS_TAB = (By.XPATH, "//span[normalize-space()='Начинки']")

    CURRENT_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    BREAD = (By.XPATH, "//h2[normalize-space()='Булки']/following-sibling::ul")
    SAUCES = (By.XPATH, "//h2[normalize-space()='Соусы']/following-sibling::ul")
    TOPPINGS = (By.XPATH, "//h2[normalize-space()='Начинки']/following-sibling::ul")
    CREATE = (By.XPATH, "//h1[text()='Соберите бургер']")
    LINK_CONSTRUCT = (By.XPATH, "//p[text()='Конструктор']/parent::a[1]")