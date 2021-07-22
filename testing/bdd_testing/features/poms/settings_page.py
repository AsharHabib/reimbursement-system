class SettingsPage():
    reset_link = 'reset-password'

    def __init__(self, driver):
        self.driver = driver

    def click_reset_link(self):
        self.driver.find_element_by_id(self.reset_link).click()