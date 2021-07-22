import pyotp


class TwoFactorPage():
    otp_input = 'otp'
    otp_button = 'otp-button'
    secret_key = 'secret-key'

    def __init__(self, driver):
        self.driver = driver

    def enter_otp(self):
        secret = self.driver.find_element_by_id(self.secret_key).get_attribute('value')
        otp = pyotp.TOTP(secret).now()
        self.driver.find_element_by_id(self.otp_input).send_keys(otp)

    def click_otp_button(self):
        self.driver.find_element_by_id(self.otp_button).click()