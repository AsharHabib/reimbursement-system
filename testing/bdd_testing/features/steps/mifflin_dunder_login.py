from behave import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@given('A user is on the pre login page')
def test_on_pre_login(context):
    context.driver.get('http://localhost:5000/pre_login')

@given('The user clicks on the Login as employee link')
def test_user_clicks_employee_link(context):
    context.pre_login.click_employee_login_link()

@given('The user enters the correct username and password as employee')
def test_user_enters_employee_credentials(context):
    context.employee_login.enter_credentials()

@given('The user clicks submit button as employee')
def test_user_pushes_employee_login_button(context):
    context.employee_login.click_login_button()

@when('The user enters the OTP as employee')
def test_user_enters_employee_otp(context):
    context.two_factor.enter_otp()

@when('The user clicks the Authenticate User button as employee')
def test_user_clicks_employee_authenticate_button(context):
    context.two_factor.click_otp_button()

@then('The user is redirected to their employee profile')
def test_user_redirected_to_employee_profile(context):
    element = WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, 'profile-link')))
    assert 'profile' in context.driver.current_url



@given('The user clicks on the Login as manager link')
def test_user_clicks_manager_link(context):
    context.pre_login.click_manager_login_link()

@given('The user enters the correct username and password as manager')
def test_user_enters_manager_credentials(context):
    context.manager_login.enter_credentials()

@given('The user clicks submit button as manager')
def test_user_pushes_manager_login_button(context):
    context.manager_login.click_login_button()

@when('The user enters the OTP as manager')
def test_user_enters_manager_otp(context):
    context.two_factor.enter_otp()

@when('The user clicks the Authenticate User button as manager')
def test_user_clicks_manager_authenticate_button(context):
    context.two_factor.click_otp_button()

@then('The user is redirected to their manager profile')
def test_user_redirected_to_manager_profile(context):
    element = WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, 'profile-link')))
    assert 'profile' in context.driver.current_url