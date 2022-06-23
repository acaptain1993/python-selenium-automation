from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

color_options = (By.CSS_SELECTOR, "#variation_color_name li")
color_name = (By.CSS_SELECTOR, "div[id*= 'color'] span[class = 'selection']")


@given('Product {product_id} Page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Click and Verify Each Color Option')
def cycle_through_options(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown', 'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray', 'Green', 'Khaki', 'Light-green', 'Pink', 'Purple', 'Red', 'Rose Red', 'White', 'Yellow']
    result_colors = []
    color_selected = context.driver.find_elements(*color_options)

    for colors in color_selected:
        colors.click()
        color_name_for_list = context.driver.find_element(*color_name).text
        result_colors += [color_name_for_list]

    assert expected_colors == result_colors, f"Expected result is{expected_colors}\n Actual result is {result_colors}"