from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class OffPlanPage(Page):
    SEARCH_AND_FILTERS_BTN = (By.CSS_SELECTOR, ".hidden [data-test-id='search-and-filters-button']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "[data-test-id='all-filters-submit']")
    PROJECT_CARDS = (By.CSS_SELECTOR, "[href*='projects']")

    def get_status_locator(self, status):
        formatted = status.lower().replace(' ','_')
        return (By.CSS_SELECTOR, f"[data-test-id='filter-badge-{formatted}']")

    def verify_off_plan_opens(self):
        self.verify_partial_url('find')

    def filter_by_status(self, status):
        self.wait_until_clickable_click(*self.SEARCH_AND_FILTERS_BTN)

        locator = self.get_status_locator(status)
        self.scroll_to_element(*locator)
        sleep(1)
        self.wait_until_clickable_click(*locator)
        sleep(1)

        self.wait_until_clickable_click(*self.SUBMIT_BTN)

    def verify_product_status(self, status):
        project_cards = self.driver.find_elements(*self.PROJECT_CARDS)

        assert project_cards, "No project cards found after filtering"

        for index, card in enumerate(project_cards, start=1):
            statuses = card.find_element(By.XPATH, f"//*[text()='{status}']")
            assert statuses, f"Card #{index} does not contain '{status}' status"