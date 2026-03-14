from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SETTINGS_OPT = (By.CSS_SELECTOR, "ul a[href*='settings']")

    def click_settings(self):
        self.wait_until_clickable_click(*self.SETTINGS_OPT)