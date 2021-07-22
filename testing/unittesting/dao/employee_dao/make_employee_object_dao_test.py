#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.employee_dao.make_employee_object_dao import make_employee_object

class TestMakeEmployeeObjectDAO(MockDB):
    def test_dao_retrieves_all_employee_data(self):
        """This will succeed because both data sets match, testing that we do retrieve all employee data given his/her
        username"""
        self.dao_employee_object = make_employee_object('JimHalpert', productionDB=False)
        self.assertEqual(self.test_employee_object, self.dao_employee_object, "The data sets were not equal")