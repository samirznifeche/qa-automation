from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    SETTINGS_OPT = (By.CSS_SELECTOR, "ul a[href*='settings']")
    OFF_PLAN_OPT = (By.XPATH, "//ul//span[text()='Off-plan']")

    def click_settings(self):
        self.wait_until_clickable_click(*self.SETTINGS_OPT)

    def click_off_plan(self):
        self.wait_until_clickable_click(*self.OFF_PLAN_OPT)