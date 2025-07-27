import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from data.user import PersonData

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service("C:/Users/Татьяна/WebDriver/bin/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://stellarburgers.nomoreparties.site"

@pytest.fixture
def valid_user_credentials():
    path = os.path.join(os.path.dirname(__file__), "last_user.txt")
    with open(path, "r", encoding="utf-8") as f:
        email, password = f.read().strip().split(",")
    return {"email": email, "password": password}


@pytest.fixture
def login():
    return {
        "email": PersonData.login,
        "password": PersonData.password
    }