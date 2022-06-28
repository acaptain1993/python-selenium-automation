from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class MainPage(Page):


    def open_main_page(self):
        self.open_page('https://www.amazon.com/')

    def find_and_click(self, *locator):
        self.find_element(*locator)
        self.click(*locator)

    def add_to_cart(self):
        cart = self.find_element(By.ID, 'add-to-cart-button')
        cart.click()

    def hover_second_bar(self, *locator):
        actions = ActionChains(self.driver)
        hoverable = self.driver.find_element(*locator)
        actions.move_to_element(hoverable)
        actions.perform()
