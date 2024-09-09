from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class MainPage(Page):

    CLICK_USER_ICON = (By.CSS_SELECTOR, ".menu-img-agent-listing")

    def open(self):
        self.open_url('https://soft.reelly.io')

    def click_user_icon(self):
        sleep(3)
        self.wait_and_click(self.CLICK_USER_ICON)

