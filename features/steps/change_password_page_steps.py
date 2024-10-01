from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@when('Add some test password to the input fields')
def add_test_passwords(context):
    context.app.change_password_page.enter_new_password("Newpassword123")
    context.app.change_password_page.enter_repeat_password("Newpassword123")


@then("Verify the 'Change password' button is available")
def verify_change_password_button(context):
    context.app.change_password_page.verify_change_password_btn()


@then('Verify the change password page opens')
def verify_change_password_page(context):
    context.app.change_password_page.verify_change_password_page()

