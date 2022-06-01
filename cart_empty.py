from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/aaron/Documents/PythonProjects/python-selenium-automation/chromedriver.exe')

driver.get('https://www.amazon.com/')
find_cart = driver.find_element(By.CSS_SELECTOR, '#nav-cart')
find_cart.click()

expected_result = 'Your Amazon Cart is empty'
actual_result = driver.find_element(By.XPATH, "//div[contains(@class, 'sc-your-amazon')]/h2").text

assert expected_result == actual_result, f'Error! Actual test {actual_result} does not match {expected_result}'

print('Test case passed')