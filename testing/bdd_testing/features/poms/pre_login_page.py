class PreLoginPage():
    employee_login = 'employee-login-link'
    manager_login = 'manager-login-link'

    def __init__(self, driver):
        self.driver = driver

    def click_employee_login_link(self):
        self.driver.find_element_by_id(self.employee_login).click()

    def click_manager_login_link(self):
        self.driver.find_element_by_id(self.manager_login).click()