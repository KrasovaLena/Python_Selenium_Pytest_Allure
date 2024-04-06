from faker import Faker

faker_en = Faker('en_US')
Faker.seed()
first_name = faker_en.first_name_female()
last_name = faker_en.last_name_female()
postal_code = faker_en.postalcode()

main_url = 'https://www.saucedemo.com'
main_page_url = 'https://www.saucedemo.com/inventory.html'
invertory_item = 'https://www.saucedemo.com/inventory-item.html?id=4'
cart_url = 'https://www.saucedemo.com/cart.html'
checkout_1 = 'https://www.saucedemo.com/checkout-step-one.html'
checkout_2 = 'https://www.saucedemo.com/checkout-step-two.html'
checkout_complete = 'https://www.saucedemo.com/checkout-complete.html'
login = 'standard_user'
password = 'secret_sauce'
wrong_data = 'user'