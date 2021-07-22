from behave import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@given('An employee is logged in and on the profile page')
def test_employee_logged_in_and_on_profile(context):
    context.driver.get('http://localhost:5000/pre_login')
    context.pre_login.click_employee_login_link()
    context.employee_login.enter_credentials()
    context.employee_login.click_login_button()
    context.two_factor.enter_otp()
    context.two_factor.click_otp_button()
    assert 'profile' in context.driver.current_url

@when('An employee clicks on the Reimbursement Requests link')
def test_employee_clicks_reimbursement_requests_link(context):
    context.profile.click_reimbursement_requests_link()

@then('The employee is redirected to the Reimbursement Requests page')
def test_employee_redirected_to_reimbursement_requests_page(context):
    assert 'requests' in context.driver.current_url

@given('An employee is on the Reimbursement Requests page')
def test_employee_on_reimbursement_request_page(context):
    context.profile.click_reimbursement_requests_link()

@when('The employee clicks on the Submit new reimbursement request link')
def test_employee_clicks_submit_new_request_link(context):
    WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'tr')))
    context.old_requests = context.employee_made_requests.find_all_table_rows()
    context.employee_made_requests.click_submit_request_link()

@when('The employee fills in the Amount and Reason fields')
def test_employee_fills_amount_reason(context):
    context.submit_request.enter_amount_reason()

@when('The employee clicks on the Submit Request button')
def test_employee_clicks_submit_request_button(context):
    context.submit_request.click_form_submit()

@then('The new reimbursement request is added to the page')
def test_new_request_is_added(context):
    WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'tr')))
    context.new_requests = context.employee_made_requests.find_all_table_rows()
    assert len(context.new_requests) == len(context.old_requests) + 1

@then('The employee can delete the new reimbursement')
def test_new_request_deleted(context):
    context.employee_made_requests.click_delete_checkbox()

@when('The employee uploads a file')
def test_employee_uploads_file(context):
    context.submit_request.upload_request_file()

@when('The employee clicks on the Upload File button')
def test_employee_clicks_upload_file(context):
    context.submit_request.click_file_submit()
