from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class OffPlanPage(Page):
    FILTERS_BTN = (By.CSS_SELECTOR, ".hidden [data-test-id='search-and-filters-button']")
    ANNOUNCED_STATUS = (By.CSS_SELECTOR, "[data-test-id='filter-badge-announced']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "[data-test-id='all-filters-submit']")
    PROJECT_CARDS = (By.CSS_SELECTOR, "[href*='projects']")

    def verify_off_plan_opens(self):
        self.verify_partial_url('find')

    def filter_by_announced(self):
        self.wait_until_clickable_click(*self.FILTERS_BTN)
        self.scroll_to_element(*self.ANNOUNCED_STATUS)
        self.wait_until_clickable_click(*self.ANNOUNCED_STATUS)
        self.wait_until_clickable_click(*self.SUBMIT_BTN)

    def verify_announced_badge(self):
        project_cards = self.driver.find_elements(*self.PROJECT_CARDS)

        assert project_cards, "No project cards found after filtering"

        for index, card in enumerate(project_cards, start=1):
            statuses = card.find_elements(By.CSS_SELECTOR, "[data-test-id='project-card-sale-status']")
            assert statuses, f"Card #{index} does not contain 'Announced' status"