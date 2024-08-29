from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class SettingsPage(Page):

    CONTACT_US_BTN = (By.CSS_SELECTOR, "[href='/contact-us'].page-setting-block")

    def click_contact_us(self):
        sleep(3)
        self.click(*self.CONTACT_US_BTN)

