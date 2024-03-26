import time
from faker import Faker
from selenium import webdriver 
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
faker_en = Faker('en_US')
Faker.seed()

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

# def test_add_item_to_cart():
#     browser.get('https://www.saucedemo.com')

#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     time.sleep(2)
#     browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
#     assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text == '1'

#     browser.quit()

# def test_delete_item_from_cart():
#     browser.get('https://www.saucedemo.com')

#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     time.sleep(2)
#     browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
#     browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
#     assert browser.current_url == 'https://www.saucedemo.com/cart.html'
#     browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
#     assert browser.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]').text == ''
    
#     browser.quit()

# def test_add_delete_item_to_cart_from_card():
#     browser.get('https://www.saucedemo.com')

#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    
#     browser.get('https://www.saucedemo.com/inventory-item.html?id=4')
#     time.sleep(2)
#     browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
#     assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text == '1'
#     time.sleep(2)
#     browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
#     assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').text == ''

#     browser.quit()


######################## Карточка товара ########################
    
# def test_open_item_card_picture():
#     browser.get('https://www.saucedemo.com')

#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     time.sleep(2)
#     browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()
#     time.sleep(2)
#     assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'

#     browser.quit()

# def test_open_item_card_title():
#     browser.get('https://www.saucedemo.com')

#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     time.sleep(2)
#     browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
#     time.sleep(2)
#     assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'

#     browser.quit()

######################## Оформление заказа ########################

# def test_checkout():
#     browser.get('https://www.saucedemo.com')
    
#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     time.sleep(2)
#     browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
#     browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
#     assert browser.current_url == 'https://www.saucedemo.com/cart.html'
#     browser.find_element(By.XPATH, '//*[@id="checkout"]').click()
#     assert browser.current_url == 'https://www.saucedemo.com/checkout-step-one.html'
#     first_name = faker_en.first_name_female()
#     last_name = faker_en.last_name_female()
#     postal_code = faker_en.postalcode()
#     browser.find_element('xpath', '//*[@id="first-name"]').send_keys(f'{first_name}')
#     browser.find_element('xpath', '//*[@id="last-name"]').send_keys(f'{last_name}')
#     browser.find_element('xpath', '//*[@id="postal-code"]').send_keys(f'{postal_code}')
#     browser.find_element(By.XPATH, '//*[@id="continue"]').click()
#     assert browser.current_url == 'https://www.saucedemo.com/checkout-step-two.html'
#     browser.find_element(By.XPATH, '//*[@id="finish"]').click()
#     assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html'
    
#     browser.quit()

######################## Фильтр ########################
    
# def test_filter():
#     browser.get('https://www.saucedemo.com')
    
#     browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
#     browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
#     browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
#     browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]').click()
#     assert browser.find_element(By.XPATH, '(//*[@class="inventory_item_name "])[1]').text == 'Sauce Labs Backpack'
#     time.sleep(3)
#     browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]').click()
#     assert browser.find_element(By.XPATH, '(//*[@class="inventory_item_name "])[1]').text == 'Test.allTheThings() T-Shirt (Red)'
#     time.sleep(3)
#     browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]').click()
#     assert browser.find_element(By.XPATH, '(//*[@class="inventory_item_price"])[1]').text == '$7.99'
#     time.sleep(3)
#     browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').click()
#     assert browser.find_element(By.XPATH, '(//*[@class="inventory_item_price"])[1]').text == '$49.99'
#     time.sleep(3)

######################## Бургер меню ########################



