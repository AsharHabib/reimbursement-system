from behave import *

@given('The user is on the Login Page')
def test_user_on_login_page(context):
    context.driver.get('http://localhost:5000/login?is_employee=True')

@given('The user clicks on Forgot username?')
def test_user_clicks_forgot_username(context):
    context.employee_login.click_forgot_username()

@when('The user inputs their first name and last name')
def test_user_inputs_first_last_names(context):
    context.resend_username.enter_names()

@when('The user clicks the Resend username button')
def test_user_clicks_resend_username(context):
    context.resend_username.click_resend_button()

@then('The user is redirected to a page telling them the username email was sent')
def test_redirected_and_username_email_sent(context):
    assert context.driver.find_element_by_id('h1-header').text == """Your username has been sent to your email."""
    context.driver.get('http://localhost:5000/pre_login')
    context.pre_login.click_employee_login_link()
    context.employee_login.enter_credentials()
    context.employee_login.click_login_button()
    context.two_factor.enter_otp()
    context.two_factor.click_otp_button()

@given('The user clicks on Forgot password?')
def test_user_clicks_forgot_password(context):
    context.employee_login.click_forgot_password()

@when('The user inputs their username')
def test_user_inputs_username(context):
    context.reset_password.enter_username()

@when('The user clicks the Reset password button')
def test_user_clicks_reset_password(context):
    context.reset_password.click_reset_button()

@when('The user enters the OTP')
def test_user_enters_otp(context):
    context.two_factor.enter_otp()

@when('The user clicks the Authenticate User button')
def test_user_clicks_authenticate_button(context):
    context.two_factor.click_otp_button()

@then('The user is redirected to a page telling them the password email was sent')
def test_redirected_and_password_email_sent(context):
    assert context.driver.find_element_by_id('h2-header').text == 'An email has been sent to you to reset your password, the link expires in 1 hour.'
    context.driver.get('http://localhost:5000/pre_login')
    context.pre_login.click_employee_login_link()
    context.employee_login.enter_credentials()
    context.employee_login.click_login_button()
    context.two_factor.enter_otp()
    context.two_factor.click_otp_button()

@given('The user logs in')
def test_user_logs_in(context):
    context.driver.get('http://localhost:5000/pre_login')
    context.pre_login.click_employee_login_link()
    context.employee_login.enter_credentials()
    context.employee_login.click_login_button()
    context.two_factor.enter_otp()
    context.two_factor.click_otp_button()

@given('The user clicks on Settings')
def test_user_clicks_settings(context):
    context.profile.click_settings_link()

@when('The user clicks on the Send email link')
def test_user_clicks_send_email_link(context):
    context.settings.click_reset_link()

@then('The user is redirected to a page telling them the password email was sent again')
def test_redirected_and_password_email_sent_again(context):
    assert context.driver.find_element_by_id('h2-header').text == 'An email has been sent to you to reset your password, the link expires in 1 hour.'