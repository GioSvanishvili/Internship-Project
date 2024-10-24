from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class SecondaryOption(Page):

    PAGE_COUNT = (By.CSS_SELECTOR, ".page-count[wized='totalPageProperties']")
    CURRENT_PAGE_COUNT = (By.CSS_SELECTOR, ".page-count[wized='currentPageProperties']")
    PAGINATION_FORWARD_BTN = (By.CSS_SELECTOR, "[wized='nextPageMLS']")
    PAGINATION_PREVIOUS_BTN = (By.CSS_SELECTOR, "[wized='previousPageMLS']")
    SECONDARY_LISTINGS_URL = 'https://soft.reelly.io/secondary-listings'

    def go_to_final_page(self):
        current_page = 1
        total_pages_str = self.driver.find_element(*self.PAGE_COUNT).text
        total_pages_int = int(total_pages_str)

        while current_page < total_pages_int:
            self.wait_for_element_appear(self.PAGE_COUNT)
            self.wait_and_click(self.PAGINATION_FORWARD_BTN)
            current_page += 1

    def go_to_first_page(self):
        clicks_to_first_page = 1
        total_pages_str = self.driver.find_element(*self.PAGE_COUNT).text
        total_pages_int = int(total_pages_str)

        while clicks_to_first_page < total_pages_int:
            self.wait_for_element_appear(self.PAGE_COUNT)
            self.wait_and_click(self.PAGINATION_PREVIOUS_BTN)
            clicks_to_first_page += 1

    def verify_secondary_listing_url(self):
        sleep(2)
        self.verify_url(self.SECONDARY_LISTINGS_URL)

