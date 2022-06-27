from pages.base_page import Page
from selenium.webdriver.common.by import By


class Signin(Page):
    ACTUAL_TEXT = (By.CSS_SELECTOR, "h1")

    def verify_page(self):
        actual_text = self.context.driver.find_element(*self.ACTUAL_TEXT).text
        expected_text = 'Sign-In'
        assert actual_text == expected_text, f"{expected_text} should be text, instead {actual_text} is text"
