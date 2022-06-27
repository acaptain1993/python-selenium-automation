from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    FIND_CART = (By.CSS_SELECTOR, '#nav-cart')
    ORDER_LINK = (By.CSS_SELECTOR, "#nav-orders")

    def search_amazon(self, text):
        self.input_text(text, *self.SEARCH_BAR)
        self.click(*self.SEARCH_BTN)



    def click_cart(self):
        self.click(*self.FIND_CART)

    def click_orders_link(self):
        self.click(*self.ORDER_LINK)



