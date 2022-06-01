from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:/Users/aaron/Documents/PythonProjects/python-selenium-automation'
                                          '/chromedriver.exe')

driver.get('https://www.amazon.com/hz/contact-us/foresight/hubgateway')

driver.find_element(By.XPATH, "//input[@maxlength ='500']").send_keys('Cancel Order', Keys.ENTER)

expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//a[@name = 'GUID-159D403A-3B08-477C-88E3-58C737822D49']/../h1").text

assert expected_result == actual_result, f'Error! Actual test {actual_result} does not match {expected_result}'

print('Test case passed')
driver.quit()