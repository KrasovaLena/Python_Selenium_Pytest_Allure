from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage():

    def __init__(self, browser: webdriver, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 10)
    
    def open(self):
        return self.browser.get(self.url)

    def is_visible(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_invisible(self, locator) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def text_in_element(self, locator, str) -> WebElement:
        return self.wait.until(EC.text_to_be_present_in_element(locator, str))

    def is_clickable(self, locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    


    

