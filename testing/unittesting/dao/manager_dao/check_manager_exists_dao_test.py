#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.manager_dao.check_manager_exists_dao import check_manager_exists

class TestCheckManagerExistsDAO(MockDB):
    def test_dao_returns_manager_usernames_passwords(self):
        """This will succeed because the DAO returns the usernames and passwords, which match what we got in MockDB's
        setUp, tests that we get all usernames and passwords from the managers table"""
        self.dao_manager_usernames_passwords = check_manager_exists(productionDB=False)
        self.assertCountEqual(self.test_check_manager_exists, self.dao_manager_usernames_passwords, """The arguments
        do not exactly match""")