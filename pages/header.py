from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Header(Page):
    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    FIND_CART = (By.CSS_SELECTOR, '#nav-cart')
    ORDER_LINK = (By.CSS_SELECTOR, "#nav-orders")
    DEPARTMENT = (By.CSS_SELECTOR, "#searchDropdownBox")


    def search_amazon(self, text):
        self.input_text(text, *self.SEARCH_BAR)
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.click(*self.FIND_CART)

    def click_orders_link(self):
        self.click(*self.ORDER_LINK)

    def change_department(self):
        actions = ActionChains(self.driver)
        departments = self.driver.find_element(*self.DEPARTMENT)
        actions.move_to_element(departments)
        actions.perform()

    def click_department(self, *locator):
        #clickable = self.driver.find_element(*locator)
        #clickable.click()
        self.click(*locator)

    def verify_department(self, expected_text,*locator):
        expectation = expected_text
        item = self.convert_to_text(*locator)
        assert expectation == item, f"Text did not match, cart has {item} instead of {expectation}"

