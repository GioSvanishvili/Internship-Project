from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@given('Open the main page')
def open_reelly(context):
    context.app.main_page.open()


