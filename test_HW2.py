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

    browser.find_element(By.XPATH, username_field).send_keys(login)
    browser.find_element(By.XPATH, password_field).send_keys(password)
    browser.find_element(By.XPATH, login_button).click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'


def test_auth_negative(browser):
    browser.get(main_url)

    browser.find_element(By.XPATH, username_field).send_keys(wrong_data)
    browser.find_element(By.XPATH, password_field).send_keys(wrong_data)
    browser.find_element(By.XPATH, login_button).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//h3[contains(@data-test, "error")]').is_displayed


####################### Корзина ########################

def test_add_item_to_cart(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, add_backpack_to_cart).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text == '1'

def test_delete_item_from_cart(browser):
    
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, add_backpack_to_cart).click()
    time.sleep(2)
    browser.find_element(By.XPATH, shopping_cart).click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/cart.html'
    browser.find_element(By.XPATH, remove_backpack_from_cart).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]').text == ''


def test_add_remove_item_to_cart_from_card(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.get(invertory_item)
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
    browser.find_element(By.XPATH, item_picture).click()
    time.sleep(2)
    assert browser.current_url == invertory_item


def test_open_item_card_title(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, item_title).click()
    time.sleep(2)
    assert browser.current_url == invertory_item


####################### Оформление заказа ########################

def test_checkout(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, add_backpack_to_cart).click()
    time.sleep(2)
    browser.find_element(By.XPATH, shopping_cart).click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/cart.html'
    browser.find_element(By.XPATH, checkout_button).click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/checkout-step-one.html'
    browser.find_element(By.XPATH, first_name_field).send_keys(f'{first_name}')
    browser.find_element(By.XPATH, last_name_field).send_keys(f'{last_name}')
    browser.find_element(By.XPATH, postal_code_field).send_keys(f'{postal_code}')
    browser.find_element(By.XPATH, continue_button).click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/checkout-step-two.html'
    browser.find_element(By.XPATH, finish_button).click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html'


####################### Фильтр ########################
    
def test_filter_A_to_Z(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, filter_A_to_Z).click()
    time.sleep(2)
    elements = browser.find_elements(By.XPATH, inventory_item_name)
    elements = [element.text for element in elements]
    elements_ordered = sorted(elements)
    assert elements == elements_ordered



def test_filter_Z_to_A(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, filter_Z_to_A).click()
    time.sleep(2)
    elements = browser.find_elements(By.XPATH, inventory_item_name)
    elements = [element.text for element in elements]
    elements_ordered = sorted(elements, reverse=True)
    assert elements == elements_ordered
    

def test_filter_low_to_high(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, filter_low_to_high).click()
    time.sleep(2)
    elements = browser.find_elements(By.XPATH, inventory_item_price)
    elements = [float(element.text[1:]) for element in elements]
    elements_ordered = sorted(elements)
    assert elements == elements_ordered
    

def test_filter_high_to_low(browser):

    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, filter_high_to_low).click()
    time.sleep(2)
    elements = browser.find_elements(By.XPATH, inventory_item_price)
    elements = [float(element.text[1:]) for element in elements]
    elements_ordered = sorted(elements, reverse=True)
    assert elements == elements_ordered

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
