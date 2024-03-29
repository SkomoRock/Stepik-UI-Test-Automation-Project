from .locators import BasePageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, browser, url, timeout = 4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try: self.browser.find_element(how, what)
        except NoSuchElementException: return False
        return True

    def is_not_element_present(self, how, what, timeout = 4):
        try: WebDriverWait(self.browser, timeout).\
            until(EC.presence_of_element_located((how, what)))
        except TimeoutException: return True
        return False

    def is_disappeared(self, how, what, timeout = 4):
        try: WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException: return False
        return True

    def go_to_login_page(self):
        try:
            link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
            link.click()
        except: assert False, 'Go to login page is FAILED'

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            'Login link is NOT FOUND'

    def go_to_basket(self):
        try:
            link = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
            link.click()
        except: assert False, 'Go to basket is FAILED'

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            'User icon is NOT FOUND, probably UNAUTHORISED user'
