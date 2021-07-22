class ManagerRequestsPage():
    status_request = 'status-1-1'
    update_button = 'update-requests-button'
    rejected_status = 'rejected-1-1-0'
    manager_message = 'manager-message-1-1-0'

    def __init__(self, driver):
        self.driver = driver

    def update_status(self):
        self.driver.find_element_by_id(self.rejected_status).click()

    def add_optional_message(self):
        self.driver.find_element_by_id(self.manager_message).send_keys('N/A')

    def click_update_button(self):
        self.driver.find_element_by_id(self.update_button).click()

    def get_status(self):
        return self.driver.find_element_by_id(self.status_request).text