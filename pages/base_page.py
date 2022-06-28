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

    def compare(self, expected, list, list_item):
        expectation = expected
        results = []
        item_list = self.driver.find_element(list)

        for item in item_list:
            item_name = self.driver.find_element(list_item)
            results += [item_name]

        assert expectation == results, f"{expectation} was expected, instead received {results}"

