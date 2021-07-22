class ResendUsernamePage():
    first_name_input = 'resend_first_name'
    last_name_input = 'resend_last_name'
    resend_button = 'resend-username-button'

    def __init__(self, driver):
        self.driver = driver

    def enter_names(self):
        self.driver.find_element_by_id(self.first_name_input).send_keys('A')
        self.driver.find_element_by_id(self.last_name_input).send_keys('J')

    def click_resend_button(self):
        self.driver.find_element_by_id(self.resend_button).click()