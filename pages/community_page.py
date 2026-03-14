from pages.base_page import Page
from selenium.webdriver.common.by import By


class CommunityPage(Page):
    SUPPORT_BTN = (By.CSS_SELECTOR, ".support")

    def verify_right_page(self):
        self.verify_partial_url('community')

    def verify_support_button(self):
        self.wait_until_clickable(*self.SUPPORT_BTN)