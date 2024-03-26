import time
from selenium import webdriver 
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
######################## Авторизация ########################

# def test_auth_positive():
#     browser.get('https://www.saucedemo.com')

#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

#     browser.quit()

# def test_auth_negative():
#     browser.get('https://www.saucedemo.com')
#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     assert browser.find_element(By.XPATH, '//h3[contains(@data-test, "error")]').is_displayed

#     browser.quit()

######################## Корзина ########################

def test_add_item_to_cart():
    browser.get('https://www.saucedemo.com')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text == '1'

    browser.quit()