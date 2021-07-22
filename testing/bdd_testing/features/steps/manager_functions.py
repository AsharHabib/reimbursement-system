from behave import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@given('A manager is logged in')
def test_manager_logged_in(context):
    context.driver.get('http://localhost:5000/pre_login')
    context.pre_login.click_manager_login_link()
    context.manager_login.enter_credentials()
    context.manager_login.click_login_button()
    context.two_factor.enter_otp()
    context.two_factor.click_otp_button()

@given('The manager is on the profile page')
def test_manager_on_profile_page(context):
    context.old_employees = context.profile.get_all_employees()
    assert 'profile' in context.driver.current_url

@when('A manager clicks on the Reimbursement Requests link')
def test_manager_clicks_reimbursement_requests_link(context):
    context.profile.click_reimbursement_requests_link()

@then('The manager is redirected to the Reimbursement Requests page')
def test_manager_redirected_to_reimbursement_requests_page(context):
    assert 'requests' in context.driver.current_url

@given('A manager is on the Reimbursement Requests page')
def test_employee_on_reimbursement_request_page(context):
    context.profile.click_reimbursement_requests_link()
    assert 'requests' in context.driver.current_url

@when('The manager changes the status for a request')
def test_manager_changes_status(context):
    context.manager_requests.update_status()

@when('The manager adds an optional message')
def test_manager_adds_message(context):
    context.manager_requests.add_optional_message()

@when('The manager clicks the form button')
def test_manager_clicks_form_button(context):
    context.manager_requests.click_update_button()

@then('The updates are reflected for the particular request')
def test_updates_reflected_for_request(context):
    assert context.manager_requests.get_status() == 'Rejected'

@given('A manager is on the Sign Up page')
def test_manager_on_signup_page(context):
    context.profile.click_signup_link()
    assert 'signup' in context.driver.current_url

@when("The manager inputs all the new account's information")
def test_manager_inputs_account_info(context):
    context.manager_signup.input_new_account_details()

@when('The manager clicks on the signup button')
def test_manager_clicks_signup_button(context):
    context.manager_signup.click_signup_button()

@then('The manager is redirected to the Profile page')
def test_manager_redirected_to_profile_page(context):
    assert 'profile' in context.driver.current_url

@then('The new employee is listed')
def test_new_employee_listed(context):
    context.new_employees = context.profile.get_all_employees()
    assert len(context.new_employees) == len(context.old_employees) + 1

@then('The manager can delete the new employee from the list')
def test_manager_can_delete_employee_from_list(context):
    context.profile.delete_new_employee()

@when('A manager clicks on the Statistics link')
def test_manager_clicks_statistics(context):
    context.profile.click_statistics_link()

@then('The manager is redirected to the Statistics page')
def test_manager_redirected_to_statistics_page(context):
    assert 'statistics' in context.driver.current_url