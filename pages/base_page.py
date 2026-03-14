from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://soft.reelly.io'

    def open_url(self, end_url=''):
        url = f"{self.base_url}{end_url}"
        self.driver.get(url)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_until_clickable(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable by locator {locator}"
        )

    def wait_until_clickable_click(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by locator {locator}'
        ).click()

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, \
            f"Expected '{expected_partial_url}' not in actual '{actual_url}'"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, \
            f"Expected '{expected_url}', but got actual '{actual_url}'"