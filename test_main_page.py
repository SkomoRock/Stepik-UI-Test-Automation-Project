# run command:
# py -m pytest -v --tb=line --language=en test_main_page.py

from pages.main_page import MainPage
from pages.login_page import LoginPage

main_link = 'http://selenium1py.pythonanywhere.com'
login_link = 'http://selenium1py.pythonanywhere.com/accounts/login'

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.should_be_login_link()

def test_guest_should_go_to_login_page(browser):
    page = MainPage(browser, main_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_register_form()
