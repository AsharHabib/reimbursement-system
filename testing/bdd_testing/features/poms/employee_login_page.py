class EmployeeLoginPage():
    username = 'username'
    password = 'password'
    button = 'login-button'
    forgot_username = 'forgot-username'
    forgot_password = 'forgot-password'

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self):
        self.driver.find_element_by_id(self.username).send_keys('AJ')
        self.driver.find_element_by_id(self.password).send_keys('aj')

    def click_forgot_username(self):
        self.driver.find_element_by_id(self.forgot_username).click()

    def click_forgot_password(self):
        self.driver.find_element_by_id(self.forgot_password).click()

    def click_login_button(self):
        self.driver.find_element_by_id(self.button).click()