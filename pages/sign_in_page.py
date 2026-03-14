from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email-2")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#field")
    CONTINUE_BTN = (By.XPATH, "//a[text()='Continue']")

    def open_sign_in_page(self, end_url='/sign-in'):
        self.open_url(end_url)

    def login(self, email, password):
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BTN)