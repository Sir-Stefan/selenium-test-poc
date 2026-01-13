from selenium.webdriver.common.by import By

class ExamplePage:
    URL = "https://example.com"

    HEADER = (By.TAG_NAME, "h1")
    PARAGRAPH = (By.TAG_NAME, "p")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_header_text(self):
        return self.driver.find_element(*self.HEADER).text

    def get_paragraph_text(self):
        return self.driver.find_element(*self.PARAGRAPH).text
