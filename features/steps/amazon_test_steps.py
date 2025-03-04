from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_LINK = (By.CSS_SELECTOR, "a[href*= 'amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_amazon_conditions_page(context):
    context.driver.get(f'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    print(context.driver.window_handles)


@when('Click on amazon Privacy Notice Link')
def click_link(context):
    privacy_link = context.driver.find_element(*PRIVACY_LINK)
    privacy_link.click()
    sleep(5)


@when('Switch to the newly opened window')
def switch_windows(context):
    sleep(5)
    context.driver.wait.until(EC.new_window_is_opened)
    print("\nAfter click, windows:", context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_page(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))


@then("User can close new window and switch back to original")
def close_and_switch(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
