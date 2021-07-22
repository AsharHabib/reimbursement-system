#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.employee_dao.check_employee_exists_dao import check_employee_exists

class TestCheckEmployeeExistsDAO(MockDB):
    def test_dao_returns_employee_usernames_passwords(self):
        """This will succeed because the DAO returns the usernames and passwords, which match what we got in MockDB's
        setUp, tests that we get all usernames and passwords from the managers table"""
        self.dao_employee_usernames_passwords = check_employee_exists(productionDB=False)
        self.assertCountEqual(self.test_check_employee_exists, self.dao_employee_usernames_passwords, """The arguments
        do not exactly match""")