from pages.base_page import Page
from selenium.webdriver.common.by import By


class SettingsPage(Page):
    COMMUNITY_OPT = (By.CSS_SELECTOR, "a[href*='community']")

    def click_community(self):
        self.wait_until_clickable_click(*self.COMMUNITY_OPT)