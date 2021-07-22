#Import MockDB, relevant DAO method
from testing.unittesting.mock_db import MockDB
from src.dao.user_dao.user_load_dao import user_load
from flask import session

class TestUserLoadDAO(MockDB):
    # Inherit super class's setUp, define two sample data entries from the list in the super() class
    def setUp(self):
        super().setUp()
        self.sample_employee = self.list_of_test_employees[0]
        self.sample_manager = self.list_of_test_managers[1]

    def test_employee_session_loads(self):
        """This will succeed because the contents will be equal, must first set session['account_type'] = 'Employee' to
        mimic the session getting set"""
        session['account_type'] = 'Employee'
        self.assertEqual(self.sample_employee, user_load(0), 'The test data did not match the retrieved data')
        pass

    def test_manager_session_loads(self):
        """This will succeed because the contents will be equal, must first set session['account_type'] = 'Manager' to
                mimic the session getting set"""
        session['account_type'] = 'Manager'
        self.assertEqual(self.sample_manager, user_load(1), 'The test data did not match the retrieved data')

    def tearDown(self):
        session.pop('account_type')