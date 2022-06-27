from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Click Amazon Orders Link')
def order_link_clicked(context):
    context.app.header.click_orders_link()

@then('Verify Sign In Page is Opened')
def verify_signin_page(context):
    context.app.signin.verify_page()
