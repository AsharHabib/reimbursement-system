#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.manager_dao.create_employee_account_dao import create_employee_account

class TestCreateEmployeeAccountDAO(MockDB):
    def setUp(self):
        # Inherit from super()'s setUp, select the count of all employees with manager_id of 1
        super().setUp()
        self.cur.execute('SELECT COUNT(*) FROM employees WHERE manager_id = 1')
        data = self.cur.fetchone()
        self.old_number_of_accounts = data[0]

    def test_new_employee_account_created(self):
        """This will succeed because the number of accounts increases by 1, tests if a new employee account is
        created"""
        create_employee_account(1, 'Place', 'Holder', 'username', 'password', 'Place Holder', productionDB=False)
        self.cur.execute('SELECT COUNT(*) FROM employees WHERE manager_id = 1')
        data = self.cur.fetchone()
        self.new_number_of_accounts = data[0]
        self.assertEqual(self.new_number_of_accounts - 1, self.old_number_of_accounts, """The number of accounts did 
        not change""")

    # Undo the changes and set table back to normal
    def tearDown(self):
        self.cur.execute("DELETE FROM employees WHERE employee_id = 2 AND manager_id = 1")
        super().tearDown()