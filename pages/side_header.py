from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class SideHeader(Page):

    SECONDARY_OPTION_BTN = (By.CSS_SELECTOR, "[href*='/secondary']")
    SETTINGS_BTN = (By.CSS_SELECTOR, "[href='/settings'].menu-button-block")
    CLICK_MAIN_MENU_BUTTON = (By.CSS_SELECTOR, ".circle-gradient")

    def click_settings(self):
        sleep(3)
        self.wait_and_click(self.SETTINGS_BTN)

    def click_secondary_option(self):
        sleep(3)
        self.wait_and_click(self.SECONDARY_OPTION_BTN)

    def click_main_menu(self):
        sleep(3)
        self.wait_and_click(self.CLICK_MAIN_MENU_BUTTON)

