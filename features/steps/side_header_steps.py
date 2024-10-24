from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@when('Click on Secondary listings option')
def click_secondary(context):
    context.app.side_header.click_secondary_option()


@when('Click on Settings button')
# @when('Click on Main Menu button')
def click_settings(context):
    context.app.side_header.click_settings()
# def click_main_menu(context):
#     context.app.side_header.click_main_menu()

