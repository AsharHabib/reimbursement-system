class MifflinDunderHomePage:
    home_link = 'home-link'
    pre_login_link = 'pre-login-link'

    def __init__(self, driver):
        self.driver = driver

    def click_home_link(self):
        self.driver.find_element_by_id(self.home_link).click()

    def click_login_link(self):
        self.driver.find_element_by_id(self.pre_login_link).click()