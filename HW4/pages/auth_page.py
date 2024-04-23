from pages.base_page import BasePage
from locators import *
from data import *

class LoginPage(BasePage):
    def header(self):
        return self.is_visible(header_xpath)
    
    def start_button(self):
        self.is_visible(start_button_xpath).click()
        return self
    
    def login_field(self):
        self.is_visible(login_field_xpath).send_keys(login)
        return self
    
    def password_field(self):
        self.is_visible(password_field_xpath).send_keys(password)
        return self
    
    def checkbox(self):
        self.is_visible(checkbox_xpath).click()
        return self
    
    def register_button(self):
        self.is_visible(register_button_xpath).click()
        return self
    
    def loader(self):
        return self.is_visible(loader_xpath)
        
    def success_msg(self):
        return self.is_visible(success_msg_xpath)
    