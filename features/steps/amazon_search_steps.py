from behave import given, then
from selenium.webdriver.common.by import By

starting_point = 'https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers'
best_seller_links = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a")


@given('Best Sellers Amazon')
def best_sellers_verify(context):
    context.driver.get(starting_point)


@then('Verify {expected_amount} Links Present')
def five_links_verify(context, expected_amount):
    expected_amount = int(expected_amount)
    best_seller_count = context.driver.find_elements(*best_seller_links)
    print(f"Expected Amount type: {expected_amount}")
    print(f"Best seller amount: {len(best_seller_count)}")
    assert len(best_seller_count) == 5, f"Expected 5 links but instead got {len(best_seller_count)}"
