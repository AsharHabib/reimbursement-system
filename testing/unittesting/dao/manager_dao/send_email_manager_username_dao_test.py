#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.manager_dao.send_email_manager_username_dao import send_email_manager_username

class TestSendEmailManagerUsernameDAO(MockDB):
    def test_manager_username_email_were_returned(self):
        """This will succeed because the retrieved username and email match what were already there"""
        self.dao_manager_email_username = send_email_manager_username('Michael', 'Scott', productionDB=False)
        self.assertCountEqual(self.test_manager_email_username, self.dao_manager_email_username, 'The two arguments '
                                                                                                 'were not equal')