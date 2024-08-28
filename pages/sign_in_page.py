from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class SignInPage(Page):

    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    LOGIN_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def type_email(self, email):
        self.input_text(email, *self.EMAIL_FIELD)

    def type_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def log_in_button(self):
        self.click(*self.LOGIN_BTN)

