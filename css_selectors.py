from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/aaron/Documents/PythonProjects/python-selenium-automation/chromedriver.exe')

driver.get('https://tinyurl.com/4h8sssft')
# best css_selector for amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

# best css_selector for Create Account text
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# best css_selector for your name text box
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")


# best css_selector for email text box
driver.find_element(By.CSS_SELECTOR, "#ap_email")


# best css_selector for password text
driver.find_element(By.CSS_SELECTOR, "#ap_password")


# best css_selector for password requirements
driver.find_element(By.CSS_SELECTOR, "div[class*=  'a-alert-inline-info']")


# best css_selector for re-enter password text box
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")


# best css_selector create your Amazon account / continue
driver.find_element(By.CSS_SELECTOR, "#continue")


# best css_selector for conditions of use
driver.find_element(By.CSS_SELECTOR, "div.a-section [href*='notification_condition']")


# best css_selector for privacy notice
driver.find_element(By.CSS_SELECTOR, "div.a-section [href*='notification_privacy']")


# best css_selector sign in
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap']")

