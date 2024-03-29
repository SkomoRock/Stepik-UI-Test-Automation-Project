# run command:
# py -m pytest -v --tb=line --language=en test_main_page.py
# py -m pytest -v --tb=line --language=en -m login_guest

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
# self argument must be present first
class TestLoginFromMainPage():

    def test_guest_should_see_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_should_go_to_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_should_see_login_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/accounts/login'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_order_button()
    page.should_be_continue_link()
