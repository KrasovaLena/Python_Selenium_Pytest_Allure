import pytest
from selenium import webdriver
from data import base_url
from pages.auth_page import LoginPage



@pytest.fixture()
def browser():
    print('\nBrowser runned')
    browser = webdriver.Chrome()
    yield browser
    print('\nBrowser closed')
    browser.quit()


@pytest.fixture
def login_page(browser):
    page = LoginPage(browser, base_url)
    return page