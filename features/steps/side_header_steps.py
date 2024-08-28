from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@when('Click on settings option')
def click_settings(context):
    context.app.side_header.click_settings()

