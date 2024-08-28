from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class MainPage(Page):

    def open(self):
        self.open_url('https://soft.reelly.io')

