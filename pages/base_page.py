class Page:
    def __init__(self, driver):
        self.driver = driver

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def find_element(self, *locator):
        self.driver.find_element(*locator)

    def convert_to_text(self, *locator):
        conversion = self.driver.find_element(*locator).text
        return conversion
