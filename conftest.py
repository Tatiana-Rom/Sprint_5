import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data.user import PersonData
from helpers.auth import perform_login
from data.urls import MAIN

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
    perform_login(driver, login["email"], login["password"], MAIN)
    return driver