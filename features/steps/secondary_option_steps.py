from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@then('Verify Secondary listings page opened')
def verify_secondary_listing_url(context):
    context.app.secondary_option_page.verify_secondary_listing_url()


@when('Click on pagination button and run through all the pages')
def click_pagination(context):
    context.app.secondary_option_page.go_to_final_page()
    context.app.secondary_option_page.go_to_first_page()
