class ManagerSignupPage():
    first_name_input = 'first-name'
    last_name_input = 'last-name'
    username_input = 'username'
    password_input = 'password'
    job_title_input = 'job-title'
    signup_button = 'signup-button'

    def __init__(self, driver):
        self.driver = driver

    def input_new_account_details(self):
        self.driver.find_element_by_id(self.first_name_input).send_keys('Place')
        self.driver.find_element_by_id(self.last_name_input).send_keys('Holder')
        self.driver.find_element_by_id(self.username_input).send_keys('PlaceHolder')
        self.driver.find_element_by_id(self.password_input).send_keys('placeholder')
        self.driver.find_element_by_id(self.job_title_input).send_keys('Place Holder')

    def click_signup_button(self):
        self.driver.find_element_by_id(self.signup_button).click()