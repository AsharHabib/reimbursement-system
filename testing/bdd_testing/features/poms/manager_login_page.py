class ManagerLoginPage():
    username = 'username'
    password = 'password'
    button = 'login-button'

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self):
        self.driver.find_element_by_id(self.username).send_keys('MichaelScott')
        self.driver.find_element_by_id(self.password).send_keys('michaelscott')

    def click_login_button(self):
        self.driver.find_element_by_id(self.button).click()