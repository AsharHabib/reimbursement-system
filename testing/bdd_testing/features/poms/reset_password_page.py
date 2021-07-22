class ResetPasswordPage():
    username_input = 'reset_pass_username'
    reset_button = 'reset-password-button'

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self):
        self.driver.find_element_by_id(self.username_input).send_keys('AJ')

    def click_reset_button(self):
        self.driver.find_element_by_id(self.reset_button).click()