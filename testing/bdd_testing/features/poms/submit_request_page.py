class SubmitRequestPage:
    amount_requested = 'amount-requested'
    reason_given = 'reason-given'
    form_submit = 'form-submit'

    file_upload = 'myFile'
    file_submit = 'file-submit'

    def __init__(self, driver):
        self.driver = driver

    def enter_amount_reason(self):
        self.driver.find_element_by_id(self.amount_requested).send_keys('40')
        self.driver.find_element_by_id(self.reason_given).send_keys('Some reason')

    def click_form_submit(self):
        self.driver.find_element_by_id(self.form_submit).click()

    def upload_request_file(self):
        self.driver.find_element_by_id(self.file_upload).send_keys(r"C:\Users\Ashar Habib\6-7-2021-pyjwa\P1\testing\bdd_testing" + """\\""" + 'sample_request.txt')

    def click_file_submit(self):
        self.driver.find_element_by_id(self.file_submit).click()