import time
from selenium.webdriver.common.by import By
from data import *
from locators import *


####################### Авторизация ########################

def test_auth_positive(browser):
    browser.get(main_url)
    browser.find_element(By.XPATH, username_field).send_keys(login)
    browser.find_element(By.XPATH, password_field).send_keys(password)
    browser.find_element(By.XPATH, login_button).click()
    time.sleep(2)
    assert browser.current_url == main_page_url, 'Не удалось зарегистрироваться'


def test_auth_negative(browser):
    browser.get(main_url)
    browser.find_element(By.XPATH, username_field).send_keys(wrong_data)
    browser.find_element(By.XPATH, password_field).send_keys(wrong_data)
    browser.find_element(By.XPATH, login_button).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, auth_error).is_displayed , 'Ошибка регистрации не отображена'


####################### Корзина ########################

def test_add_item_to_cart(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, add_backpack_to_cart).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, cart_container).text == '1' , 'Товар не добавлен в корзину'


def test_delete_item_from_cart(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, add_backpack_to_cart).click()
    time.sleep(2)
    browser.find_element(By.XPATH, shopping_cart).click()
    time.sleep(2)
    assert browser.current_url == cart_url, 'Не удалось перейти в корзину'
    browser.find_element(By.XPATH, remove_backpack_from_cart).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, empty_cart_container).text == '' , 'Товар не был удален из корзины'


def test_add_remove_item_to_cart_from_card(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.get(invertory_item)
    browser.find_element(By.ID, "add-to-cart").click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, cart_container).text == '1' , 'Товар не добавлен в корзину'
    browser.find_element(By.ID, "remove").click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, empty_cart_container).text == '' , 'Товар не был удален из корзины'


####################### Карточка товара ########################
    
def test_open_item_card_picture(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, item_picture).click()
    time.sleep(2)
    assert browser.current_url == invertory_item , 'Переход в карточку товара не произошел'


def test_open_item_card_title(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, item_title).click()
    time.sleep(2)
    assert browser.current_url == invertory_item , 'Переход в карточку товара не произошел'


####################### Оформление заказа ########################

def test_checkout(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, add_backpack_to_cart).click()
    time.sleep(2)
    browser.find_element(By.XPATH, shopping_cart).click()
    time.sleep(2)
    assert browser.current_url == cart_url, 'Не удалось перейти в корзину'
    browser.find_element(By.XPATH, checkout_button).click()
    time.sleep(2)
    assert browser.current_url == checkout_1, 'Не удалось перейти к оформилению заказа'
    browser.find_element(By.XPATH, first_name_field).send_keys(f'{first_name}')
    browser.find_element(By.XPATH, last_name_field).send_keys(f'{last_name}')
    browser.find_element(By.XPATH, postal_code_field).send_keys(f'{postal_code}')
    browser.find_element(By.XPATH, continue_button).click()
    time.sleep(2)
    assert browser.current_url == checkout_2, 'Не удалось продолжить оформление заказа'
    browser.find_element(By.XPATH, finish_button).click()
    time.sleep(2)
    assert browser.current_url == checkout_complete , 'Не удалось оформить заказ'


####################### Фильтр ########################
    
def test_filter_A_to_Z(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, filter_A_to_Z).click()
    time.sleep(2)
    elements = browser.find_elements(By.XPATH, inventory_item_name)
    elements = [element.text for element in elements]
    elements_ordered = sorted(elements)
    assert elements == elements_ordered , 'Фильтр A to Z работает некорректно'


def test_filter_Z_to_A(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, filter_Z_to_A).click()
    time.sleep(2)
    elements = browser.find_elements(By.XPATH, inventory_item_name)
    elements = [element.text for element in elements]
    elements_ordered = sorted(elements, reverse=True)
    assert elements == elements_ordered , 'Фильтр Z to A работает некорректно'
    

def test_filter_low_to_high(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, filter_low_to_high).click()
    time.sleep(2)
    elements = browser.find_elements(By.XPATH, inventory_item_price)
    elements = [float(element.text[1:]) for element in elements]
    elements_ordered = sorted(elements)
    assert elements == elements_ordered , 'Фильтр low to high работает некорректно'
    

def test_filter_high_to_low(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, filter_high_to_low).click()
    time.sleep(2)
    elements = browser.find_elements(By.XPATH, inventory_item_price)
    elements = [float(element.text[1:]) for element in elements]
    elements_ordered = sorted(elements, reverse=True)
    assert elements == elements_ordered , 'Фильтр high to low работает некорректно'


####################### Бургер меню ########################

def test_menu_about(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, burger_menu).click()
    time.sleep(2)
    browser.find_element(By.XPATH, about_sidebar_link).click()
    time.sleep(2)
    assert browser.current_url == 'https://saucelabs.com/', 'Кнопка About Us работает некорректно'


def test_menu_reset(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, add_backpack_to_cart).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, cart_container).text == '1', 'Корзина пуста'
    browser.find_element(By.XPATH, burger_menu).click()
    time.sleep(2)
    browser.find_element(By.XPATH, reset_sidebar_link).click()
    time.sleep(2)
    assert browser.find_element(By.XPATH, empty_cart_container).text == '' , 'Кнопка Reset работает некорректно'


def test_menu_logout(browser):
    test_auth_positive(browser)
    time.sleep(2)
    browser.find_element(By.XPATH, burger_menu).click()
    time.sleep(2)
    browser.find_element(By.XPATH, logout_sidebar_link).click()
    time.sleep(2)
    assert browser.current_url == 'https://www.saucedemo.com/', 'Кнопка Logout работает некорректно'
