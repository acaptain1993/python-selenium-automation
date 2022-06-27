from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon Page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Cart is Clicked')
def cart_clicked(context):
    #find_cart = context.driver.find_element(By.CSS_SELECTOR, '#nav-cart')
    #find_cart.click()
    context.app.header.click_cart()


@then('Verify Cart is Empty')
def verify_cart_empty(context):
    #expected_result = 'Your Amazon Cart is empty'
    #actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'sc-your-amazon')]/h2").text
    #assert expected_result == actual_result, f'Error! Actual test {actual_result} does not match {expected_result}'
    context.app.cart.verify_cart_empty()
