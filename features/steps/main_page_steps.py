from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@given('Open the main page')
def open_reelly(context):
    context.app.main_page.open()


@when('Click on User Icon')
def click_on_user_icon(context):
    context.app.main_page.click_user_icon()


