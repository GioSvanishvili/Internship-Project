from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class ChangePasswordPage(Page):

    NEW_PASSWORD_INPUT = (By.ID, "Enter-new-password")
    REPEAT_PASSWORD_INPUT = (By.ID, "Repeat-password")
    VERIFY_CHANGE_PASSWORD_BTN = (By.CSS_SELECTOR, "[wized='changePasswordButton']")
    VERIFY_CHANGE_PASSWORD_TEXT = (By.CSS_SELECTOR, ".change-password-text")

    def enter_new_password(self, new_password):
        sleep(2)
        self.input_text(new_password, *self.NEW_PASSWORD_INPUT)

    def enter_repeat_password(self, repeat_password):
        sleep(2)
        self.input_text(repeat_password, *self.REPEAT_PASSWORD_INPUT)

    def verify_change_password_page(self):
        sleep(2)
        self.verify_text("Change password", *self.VERIFY_CHANGE_PASSWORD_TEXT)

    def verify_change_password_btn(self):
        sleep(2)
        self.find_element(*self.VERIFY_CHANGE_PASSWORD_BTN)
        self.wait_until_clickable(self.VERIFY_CHANGE_PASSWORD_BTN)

