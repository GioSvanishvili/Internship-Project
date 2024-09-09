from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@when('Log in to the page')
def log_in(context):
    context.app.sign_in_page.type_email('gsvanishvili7@gmail.com')
    context.app.sign_in_page.type_password('Zuragioana27175')
    context.app.sign_in_page.log_in_button()

