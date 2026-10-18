import pytest
from selenium import webdriver
from pages.main_page import MainPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.implicitly_wait(10)

    yield driver
    driver.quit()
