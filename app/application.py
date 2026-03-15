from pages.community_page import CommunityPage
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.settings_page import SettingsPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):

        self.community_page = CommunityPage(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SignInPage(driver)