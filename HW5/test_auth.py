from selene import browser, by, have
from selene.support.shared.jquery_style import s
import allure

base_url = 'https://victoretc.github.io/selenium_waits/'


@allure.title('Test Auth')
@allure.description('The Auth steps on the base_url')
def test_auth_positive():
    browser.config.timeout = 10
    browser.open(base_url)
    s('/html/body/h1').should(have.text('Практика с ожиданиями в Selenium'))
    s('//*[@id="startTest"]').click()
    s('#login').type('login')
    s('#password').type('password')
    s('#agree').click()
    browser.element(by.text('Зарегистрироваться')).click()
    assert s('//*[@id="loader"]').should(have.text('Загрузка...'))
    assert s('#successMessage').should(have.text('Вы успешно зарегистрированы!'))