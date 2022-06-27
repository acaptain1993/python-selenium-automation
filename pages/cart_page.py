from pages.base_page import Page
from selenium.webdriver.common.by import By


class Cart (Page):
    ACTUAL_RESULT = (By.XPATH, "//div[contains(@class, 'sc-your-amazon')]/h2")
    #EXPECTED_RESULT = 'Your Amazon Cart is empty'

    def verify_cart_empty(self):
        expected_result = "Your Amazon Cart is empty"
        actual_result = self.driver.find_element(*self.ACTUAL_RESULT).text
        assert expected_result == actual_result, f'Error! Actual test {actual_result} does not match {expected_result}'

    def verify_cart_item(self, expected_text, *locator):
        expectation = expected_text
        item = self.convert_to_text(*locator)
        print(expectation)
        print(item)
        assert expectation == item, f"Text did not match, cart has {item} instead of {expectation}"
