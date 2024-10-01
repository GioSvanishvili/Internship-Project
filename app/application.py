from pages.base_page import Page
from pages.sign_in_page import SignInPage
from pages.side_header import SideHeader
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.contact_us_page import ContactUsPage
from pages.change_password_page import ChangePasswordPage


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.sign_in_page = SignInPage(driver)
        self.side_header = SideHeader(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.change_password_page = ChangePasswordPage(driver)
