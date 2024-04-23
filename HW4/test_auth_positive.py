from pages.auth_page import *

def test_auth_positive(login_page):
    login_page.open()

    login_page.header().is_displayed()

    login_page.start_button()\
        .login_field()\
        .password_field()\
        .checkbox()\
        .register_button()

    assert login_page.loader().is_displayed()
    assert login_page.success_msg().text == 'Вы успешно зарегистрированы!'