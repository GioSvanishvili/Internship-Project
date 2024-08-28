from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class ContactUsPage(Page):

    CONTACT_US_URL = 'https://soft.reelly.io/contact-us'
    SOCIAL_ICONS = (By.CSS_SELECTOR, ".contact-button.w-inline-block img.img-social")
    CONNECT_THE_COMPANY_BTN = (By.CSS_SELECTOR, ".button-link-menu._1")

    def verify_contact_us_opened(self):
        self.verify_url(self.CONTACT_US_URL)

    def verify_social_4_icons(self):
        self.find_elements(*self.SOCIAL_ICONS)

    def verify_connect_the_company_btn(self):
        self.verify_text('Connect the company', *self.CONNECT_THE_COMPANY_BTN)
        self.wait_until_clickable(self.CONNECT_THE_COMPANY_BTN)
