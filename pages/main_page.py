from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):


    def open_main_page(self):
        self.open_page('https://www.amazon.com/')

    def find_and_click(self, *locator):
        self.find_element(*locator)
        self.click(*locator)

    def add_to_cart(self):
        cart = self.find_element(By.ID, 'add-to-cart-button')
        cart.click()

