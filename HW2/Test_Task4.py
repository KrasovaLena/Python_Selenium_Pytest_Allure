import time
import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By


################### Conftest ###################
@pytest.fixture()
def browser():
    print('\nBrowser runned')
    browser = webdriver.Firefox()
    yield browser
    print('\nBrowser closed')
    browser.quit()

################### Locators ###################
checkbox1 = '#reg-term-1'
checkbox2 = '#reg-term-2'
checkbox1_confirmed = '//*[@name= "reg-term-1" and contains (@class, " checked")]'
checkbox2_confirmed = '//*[@name= "reg-term-2" and contains (@class, " checked")]'
username = 'username'
password = 'password'
agreement = 'agreement'
registerButton = 'registerButton'

################### Data ###################
qwerty = 'qwerty'
red_4pda_url = 'https://4pda.to/forum/index.php?act=auth#reg'
practice2_url = 'https://victoretc.github.io/webelements_information/'

################### Tests ###################

def test_is_selected_is_displayed(browser):
    browser.get(red_4pda_url)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, checkbox1).click()
    browser.find_element(By.CSS_SELECTOR, checkbox2).click()
    time.sleep(3)
    assert browser.find_element(By.CSS_SELECTOR, checkbox1).is_selected(), 'Первый чек-бокс не отмечен галочкой'
    assert browser.find_element(By.CSS_SELECTOR, checkbox2).is_selected(), 'Второй чек-бокс не отмечен галочкой'
    time.sleep(3)
    assert browser.find_element(By.XPATH, checkbox1_confirmed).is_displayed(), 'Условие 1 не соблюдено'
    assert browser.find_element(By.XPATH, checkbox2_confirmed).is_displayed(), 'Условие 2 не соблюдено'


def test_is_selected_is_enabled(browser):
    browser.get(practice2_url)
    time.sleep(3)
    browser.find_element(By.ID, username).send_keys(qwerty)
    browser.find_element(By.ID, password).send_keys(qwerty)
    browser.find_element(By.ID, agreement).click()
    time.sleep(3)
    assert browser.find_element(By.ID, agreement).is_selected(), 'Чек-бокс не отмечен галочкой'
    assert browser.find_element(By.ID, registerButton).is_enabled(), 'Кнопка регистрации недоступна'
