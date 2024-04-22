import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options



@pytest.fixture()
def browser():
    print('\nBrowser runned')
    browser = webdriver.Chrome()
    yield browser
    print('\nBrowser closed')
    browser.quit()


@pytest.fixture
def browser_impl_wait():
    print('\nBrowser runned')
    browser_impl_wait = webdriver.Chrome()
    browser_impl_wait.implicitly_wait(10)
    yield browser_impl_wait
    print('\nBrowser closed')
    browser_impl_wait.quit()


@pytest.fixture
def expl_wait(browser):
    expl_wait = WebDriverWait(browser, timeout=10)
    return expl_wait


