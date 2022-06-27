from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

search_bar = (By.ID, 'twotabsearchtextbox')
champion_hat = (By.XPATH, "//span[text()= '$10.97']")
add_to_cart = (By.ID, 'add-to-cart-button')
click_cart = (By.ID, 'nav-cart-count')
# hat_verification_links = (By.XPATH, "//span[contains(text(),'Champion unisex')]")
hat_verification_links = (By.XPATH, "//span[@class='a-truncate-cut']")
hat = (By.XPATH, "//span[contains(text(), 'Ameritage')]")


@when('Search for {expected_item}')
def search_for_dad_hat(context, expected_item):
    #context.driver.find_element(*search_bar).send_keys(expected_item, Keys.ENTER)
    context.app.header.search_amazon(expected_item)

@then('Click Champion Hat')
def click_champion_hat(context):
    #context.driver.find_element(By.XPATH, "//span[contains(text(), 'Ameritage')]").click()
    context.app.main_page.find_and_click(*hat)

@then('Add it to Cart')
def click_champion_hat(context):
    #context.driver.find_element(*add_to_cart).click()
    context.app.main_page.find_and_click(*add_to_cart)

@then('Cart is Clicked')
def click_champion_hat(context):
    #context.driver.find_element(*click_cart).click()
    context.app.header.click_cart()


@then('Verify Hat is There')
def hat_verify(context):
    expected_text = 'Champion unisex adult Ameritage Dad Adjustable Cap Headband, Medium Black, One Size US'
    #hat_verification = context.driver.find_element(*hat_verification_links).text
    #print(hat_verification)
    #print(type(hat_verification))
    #assert expected_text == str(hat_verification), f"Text did not match, instead {hat_verification}"
    context.app.cart_page.verify_cart_item(expected_text, *hat_verification_links)
