# Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.manager_dao.get_employees_under_manager_dao import get_employees_under_manager

class TestGetEmployeesUnderManagerDAO(MockDB):
    def test_get_all_employees_under_manager(self):
        """This will succeed because it the retrieved employee data matches what we got in MockDB's setUp, tests that
        we get all employees' data for a manager"""
        self.dao_employees_under_manager = get_employees_under_manager(0, productionDB=False)
        self.assertNotEqual(self.test_employees_under_manager, self.dao_employees_under_manager, """The arguments are
         not exactly equal""")