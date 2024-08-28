from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@then('Verify the right page opens')
def verify_contact_us_opened(context):
    context.app.contact_us_page.verify_contact_us_opened()


@then('Verify there are at least 4 social media icons')
def verify_social_icons(context):
    context.app.contact_us_page.verify_social_4_icons()


@then("Verify 'Connect the company' button is available and clickable")
def verify_connect_the_company_btn(context):
    context.app.contact_us_page.verify_connect_the_company_btn()


