import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    print('\nBrowser runned')
    browser = webdriver.Firefox()
    yield browser
    print('\nBrowser closed')
    browser.quit()
