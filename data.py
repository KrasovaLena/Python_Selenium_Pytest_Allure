from faker import Faker

faker_en = Faker('en_US')
Faker.seed()
first_name = faker_en.first_name_female()
last_name = faker_en.last_name_female()
postal_code = faker_en.postalcode()

main_url = 'https://www.saucedemo.com'
login = 'standard_user'
password = 'secret_sauce'