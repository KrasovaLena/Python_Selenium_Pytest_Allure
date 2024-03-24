# import selenium

from selenium import webdriver 
from selenium.webdriver.common.by import By
import pytest

    
driver = webdriver.Chrome()


def test_autorization(self):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.NAME, "user-name").sendKeys("standard_user")
    driver.find_element(By.NAME, "password").sendKeys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    assert driver.current_URL == "https://www.saucedemo.com/inventory.html"
    driver.quit()
        


