from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class SideHeader(Page):

    SETTINGS_BTN = (By.CSS_SELECTOR, "[href='/settings'].menu-button-block")

    def click_settings(self):
        self.click(*self.SETTINGS_BTN)

    