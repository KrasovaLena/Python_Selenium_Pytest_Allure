from selenium import webdriver 
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

def test_auth_positive():
    browser.get('https://www.saucedemo.com')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'


    browser.quit()

def test_auth_negative():
    browser.get('https://www.saucedemo.com')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.find_element(By.XPATH, '//h3[contains(@data-test, "error")]'), 'нужна другая проверка'
    
    browser.quit()