class ProfilePage():
    reimbursement_requests_link = 'requests-link'
    new_employee_account = 'employee-10'
    delete_employees_button = 'delete-employees'
    signup_link = 'signup-link'
    employees_list = 'employees-list'
    statistics_link = 'statistics-link'
    settings_link = 'settings-link'

    def __init__(self, driver):
        self.driver = driver

    def click_reimbursement_requests_link(self):
        self.driver.find_element_by_id(self.reimbursement_requests_link).click()

    def click_signup_link(self):
        self.driver.find_element_by_id(self.signup_link).click()

    def click_statistics_link(self):
        self.driver.find_element_by_id(self.statistics_link).click()

    def click_settings_link(self):
        self.driver.find_element_by_id(self.settings_link).click()

    def delete_new_employee(self):
        self.driver.find_element_by_id(self.new_employee_account).click()
        self.driver.find_element_by_id(self.delete_employees_button).click()

    def get_all_employees(self):
        return self.driver.find_element_by_id(self.employees_list).find_elements_by_tag_name('li')