from selenium.webdriver.common.by import By

# Task 1
header_xpath = (By.XPATH, '/html/body/h1')
start_button_xpath = (By.XPATH, '//*[@id="startTest"]')
login_field_xpath = (By.XPATH, '//*[@id="login"]')
password_field_xpath = (By.XPATH, '//*[@id="password"]')
checkbox_xpath = (By.XPATH, '//*[@id="agree"]')
register_button_xpath = (By.XPATH, '//*[@id="register"]')
loader_xpath = (By.XPATH, '//*[@id="loader"]')
success_msg_xpath = (By.XPATH, '//*[@id="successMessage"]')

# Task 2
add_element_button = (By.XPATH, '//*[@onclick="addElement()"]')
del_element_button = (By.XPATH, '//*[@onclick="deleteElement()"]')
congrats_msg = (By.XPATH, '//*[@class="example"]/p')