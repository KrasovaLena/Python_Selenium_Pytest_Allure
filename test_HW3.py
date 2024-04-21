import time
import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *


# def test_task1_time_sleep(browser):
#     browser.get(task1_url)
#     assert browser.find_element(*header_xpath).text == 'Практика с ожиданиями в Selenium', 'Отсутствует заголовок'
#     time.sleep(8)
#     browser.find_element(*start_button_xpath).click()
#     time.sleep(2)
#     browser.find_element(*login_field_xpath).send_keys(login)
#     browser.find_element(*password_field_xpath).send_keys(password)
#     browser.find_element(*checkbox_xpath).click()
#     assert browser.find_element(*checkbox_xpath).is_selected(), 'Не ознакомлен с правилами'
#     browser.find_element(*register_button_xpath).click()
#     time.sleep(2)
#     assert browser.find_element(*loader_xpath).is_displayed(), 'Элемент загрузки отсутствует'
#     time.sleep(5)
#     assert browser.find_element(*success_msg_xpath).text == 'Вы успешно зарегистрированы!', 'Регистрация не прошла'


# def test_task1_impl_wait(browser_impl_wait):
#     browser_impl_wait.get(task1_url)
#     assert browser_impl_wait.find_element(*header_xpath).text == 'Практика с ожиданиями в Selenium', 'Отсутствует заголовок'
#     browser_impl_wait.find_element(*start_button_xpath).click()
#     browser_impl_wait.find_element(*login_field_xpath).send_keys(login)
#     browser_impl_wait.find_element(*password_field_xpath).send_keys(password)
#     browser_impl_wait.find_element(*checkbox_xpath).click()
#     assert browser_impl_wait.find_element(*checkbox_xpath).is_selected(), 'Не ознакомлен с правилами'
#     browser_impl_wait.find_element(*register_button_xpath).click()
#     assert browser_impl_wait.find_element(*loader_xpath).is_displayed(), 'Элемент загрузки отсутствует'
#     # time.sleep(3)
#     browser_impl_wait.find_element(*success_msg_xpath).click()
#     assert browser_impl_wait.find_element(*success_msg_xpath).is_displayed(), 'Сообщение об успешной регистрации отсутствует'
#     assert browser_impl_wait.find_element(*success_msg_xpath).text == 'Вы успешно зарегистрированы!', 'Регистрация не прошла'


# def test_task1_expl_wait(browser, expl_wait): 
#     browser.get(task1_url)
#     assert expl_wait.until(EC.text_to_be_present_in_element((header_xpath), "Практика с ожиданиями в Selenium")), 'Отсутствует заголовок'
#     start_button = expl_wait.until(EC.element_to_be_clickable(start_button_xpath))
#     start_button.click()
#     input_login = expl_wait.until(EC.visibility_of_element_located(login_field_xpath))
#     input_login.send_keys(login)
#     input_password = expl_wait.until(EC.visibility_of_element_located(password_field_xpath))
#     input_password.send_keys(password)
#     checkbox = expl_wait.until(EC.visibility_of_element_located(checkbox_xpath))
#     checkbox.click()
#     assert checkbox.is_selected(), 'Не ознакомлен с правилами'
#     register_button = expl_wait.until(EC.element_to_be_clickable(register_button_xpath))
#     register_button.click()
#     loader = expl_wait.until(EC.visibility_of_element_located(loader_xpath))
#     assert loader.is_displayed(), 'Элемент загрузки отсутствует'
#     loader = expl_wait.until(EC.invisibility_of_element_located(loader_xpath))
#     assert expl_wait.until(EC.text_to_be_present_in_element((success_msg_xpath), "Вы успешно зарегистрированы!")), 'Регистрация не прошла'


# def test_task2_add_remove_elements(browser_impl_wait, expl_wait):
#     browser_impl_wait.get(task2_add_remove_elements)
#     browser_impl_wait.find_element(*add_element_button).click()
#     assert browser_impl_wait.find_element(*del_element_button).is_displayed()
#     browser_impl_wait.find_element(*del_element_button).click()
#     assert expl_wait.until(EC.invisibility_of_element_located(del_element_button))


# def test_task2_basic_auth(browser_impl_wait):
#     browser_impl_wait.get(task2_basic_auth_credentials)
#     assert browser_impl_wait.find_element(*congrats_msg).is_displayed(), 'Регистрация неудачна'


# def test_task2_broken_images(browser_impl_wait, expl_wait):



# def test_task2_checkboxes(browser_impl_wait, expl_wait):