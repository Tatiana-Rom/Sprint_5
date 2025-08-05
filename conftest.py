import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from locators.login_locators import LoginPageLocators
from locators.profile_locators import ProfilePageLocators
from data.user import PersonData
from data.urls import MAIN
from helpers.auth import LoginHelper


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login():
    return {"email": PersonData.login, "password": PersonData.password}


@pytest.fixture
def logged_in_driver(driver, login):
    driver.get(MAIN)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_FROM_MAIN_PAGE_BUTTON)
    ).click()

    LoginHelper.perform_login(driver, login["email"], login["password"])

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.ACCOUNT_BUTTON)
    )
    return driver