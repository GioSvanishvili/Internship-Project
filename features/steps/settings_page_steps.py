from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@when('Click on Contact us option')
def click_contact_us(context):
    context.app.settings_page.click_contact_us()
