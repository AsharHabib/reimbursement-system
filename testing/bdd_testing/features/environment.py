# Import webdriver, all necessary POMs
from selenium import webdriver
from poms.mifflin_dunder_home_page import MifflinDunderHomePage
from poms.pre_login_page import PreLoginPage
from poms.employee_login_page import EmployeeLoginPage
from poms.manager_login_page import ManagerLoginPage
from poms.two_factor_page import TwoFactorPage
from poms.profile_page import ProfilePage
from poms.employee_made_requests_page import EmployeeMadeRequestsPage
from poms.submit_request_page import SubmitRequestPage
from poms.manager_requests_page import ManagerRequestsPage
from poms.manager_signup_page import ManagerSignupPage
from poms.resend_username_page import ResendUsernamePage
from poms.reset_password_page import ResetPasswordPage
from poms.settings_page import SettingsPage

def before_all(context):
    # Add POM instances to context
    context.driver = webdriver.Firefox()
    context.home = MifflinDunderHomePage(context.driver)
    context.pre_login = PreLoginPage(context.driver)
    context.employee_login = EmployeeLoginPage(context.driver)
    context.manager_login = ManagerLoginPage(context.driver)
    context.two_factor = TwoFactorPage(context.driver)
    context.profile = ProfilePage(context.driver)
    context.employee_made_requests = EmployeeMadeRequestsPage(context.driver)
    context.submit_request = SubmitRequestPage(context.driver)
    context.manager_requests = ManagerRequestsPage(context.driver)
    context.manager_signup = ManagerSignupPage(context.driver)
    context.resend_username = ResendUsernamePage(context.driver)
    context.reset_password = ResetPasswordPage(context.driver)
    context.settings = SettingsPage(context.driver)


def before_step(context, step):
    context.driver.implicitly_wait(5)

def before_scenario(context, scenario):
    pass

def before_feature(context, feature):
    pass

def before_tag(context, tag):
    pass

def after_scenario(context, scenario):
    # Logout after each scenario
    context.driver.get('http://localhost:5000/logout')

def after_all(context):
    # close browser after done
    context.driver.quit()
