#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.employee_dao.send_email_employee_username_dao import send_email_employee_username

class TestSendEmailEmployeeUsernameDAO(MockDB):
    def test_employee_username_email_were_returned(self):
        """This will succeed because the retrieved username and email match what were already there"""
        self.dao_employee_email_username = send_email_employee_username('Dwight', 'Schrute', productionDB=False)
        self.assertCountEqual(self.test_employee_email_username, self.dao_employee_email_username, """The two arguments 
        were not equal""")