from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class SettingsPage(Page):

    CONTACT_US_BTN = (By.CSS_SELECTOR, "[href='/contact-us'].page-setting-block")
    CHANGE_PASSWORD_BTN = (By.XPATH, "//div[text()='Change password']")

    def click_contact_us(self):
        sleep(3)
        self.driver.execute_script("window.scrollBy(0, 500);")
        sleep(2)
        self.click(*self.CONTACT_US_BTN)

    def click_change_password(self):
        sleep(2)
        self.click(*self.CHANGE_PASSWORD_BTN)

