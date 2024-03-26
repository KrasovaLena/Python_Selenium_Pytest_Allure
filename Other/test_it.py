# import selenium

from selenium import webdriver 
from selenium.webdriver.common.by import By
import pytest

    
driver = webdriver.Chrome()


def test_autorization():
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    assert driver.current_URL == "https://www.saucedemo.com/inventory.html"
    driver.quit()
        


