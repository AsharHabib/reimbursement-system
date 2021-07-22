#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.user_dao.send_email_password_reset_dao import send_email_password_reset

class TestSendEmailPasswordResetDAO(MockDB):
    def test_manager_email_returned(self):
        """This will succeed because both rows are matching, testing that both email addresses are equal"""
        self.dao_manager_email = send_email_password_reset('MichaelScott', 'manager', productionDB=False)
        self.assertEqual(self.test_manager_email, self.dao_manager_email, 'The arguments did not match')

    def test_employee_email_returned(self):
        """This will succeed because both rows are matching, testing that both email addresses are equal"""
        self.dao_employee_email = send_email_password_reset('JimHalpert', 'employee', productionDB=False)
        self.assertEqual(self.test_employee_email, self.dao_employee_email, 'The arguments did not match')