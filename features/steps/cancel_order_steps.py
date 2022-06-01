from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep


@given('Open Amazon Customer Service')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/hz/contact-us/foresight/hubgateway')


@when('Cancel Order is Searched')
def cart_clicked(context):
    context.driver.find_element(By.XPATH, "//input[@maxlength ='500']").send_keys('Cancel Order', Keys.ENTER)


@then('Confirm Cancel Order is On Screen')
def verify_cart_empty(context):
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(By.XPATH, "//a[@name = 'GUID-159D403A-3B08-477C-88E3-58C737822D49']/../h1").text

    assert expected_result == actual_result, f'Error! Actual test {actual_result} does not match {expected_result}'
