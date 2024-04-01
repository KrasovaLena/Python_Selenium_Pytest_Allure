import time
from faker import Faker
from selenium import webdriver 
from selenium.webdriver.common.by import By
from data import *
from locators import *


faker_en = Faker('en_US')
Faker.seed()

####################### Авторизация ########################

def test_auth_positive(browser):
    browser.get(main_url)

    browser.find_element('xpath', username_field).send_keys(login)
    browser.find_element(By.XPATH, password_field).send_keys(password)
    browser.find_element(By.XPATH, login_button).click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'


def test_auth_negative(browser):
    browser.get('https://www.saucedemo.com')

    browser.find_element('xpath', username_field).send_keys('user')
    browser.find_element(By.XPATH, password_field).send_keys('user')
    browser.find_element(By.XPATH, login_button).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//h3[contains(@data-test, "error")]').is_displayed


####################### Корзина ########################

def test_add_item_to_cart(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text == '1'

def test_delete_item_from_cart(browser):
    
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/cart.html'
    browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]').text == ''


def test_add_delete_item_to_cart_from_card(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.get('https://www.saucedemo.com/inventory-item.html?id=4')
    browser.find_element(By.ID, "add-to-cart").click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text == '1'
    browser.find_element(By.ID, "remove").click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').text == ''


####################### Карточка товара ########################
    
def test_open_item_card_picture(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'


def test_open_item_card_title(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'


####################### Оформление заказа ########################

def test_checkout(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/cart.html'
    browser.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/checkout-step-one.html'
    browser.find_element('xpath', '//*[@id="first-name"]').send_keys(f'{first_name}')
    browser.find_element('xpath', '//*[@id="last-name"]').send_keys(f'{last_name}')
    browser.find_element('xpath', '//*[@id="postal-code"]').send_keys(f'{postal_code}')
    browser.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/checkout-step-two.html'
    browser.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html'


####################### Фильтр ########################
    
def test_filter(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]').click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '(//*[@class="inventory_item_name "])[1]').text == 'Sauce Labs Backpack'
    browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]').click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '(//*[@class="inventory_item_name "])[1]').text == 'Test.allTheThings() T-Shirt (Red)'
    browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]').click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '(//*[@class="inventory_item_price"])[1]').text == '$7.99'
    browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '(//*[@class="inventory_item_price"])[1]').text == '$49.99'


####################### Бургер меню ########################

def test_menu_about(browser):

    test_auth_positive(browser)
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'
    browser.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="about_sidebar_link"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://saucelabs.com/', 'url не соответствует ожидаемому'



def test_menu_reset(browser):

    test_auth_positive(browser)
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text == '1'
    browser.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="reset_sidebar_link"]').click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').text == ''


def test_menu_logout(browser):

    test_auth_positive(browser)
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'
    browser.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/', 'url не соответствует ожидаемому'





