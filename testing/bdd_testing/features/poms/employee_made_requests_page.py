class EmployeeMadeRequestsPage():
    submit_request_link = 'submit-request-link'
    checkbox_id = '2-7'
    delete_button = 'delete-button'
    requests_table = 'made-requests'

    def __init__(self, driver):
        self.driver = driver

    def click_submit_request_link(self):
        self.driver.find_element_by_id(self.submit_request_link).click()

    def click_delete_checkbox(self):
        self.driver.find_element_by_id(self.checkbox_id).click()
        self.driver.find_element_by_id(self.delete_button).click()

    def find_all_table_rows(self):
        return self.driver.find_element_by_id(self.requests_table).find_elements_by_tag_name("tr")