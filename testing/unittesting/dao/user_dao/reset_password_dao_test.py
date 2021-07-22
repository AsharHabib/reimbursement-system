#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.user_dao.reset_password_dao import reset_password

class TestResetPasswordDAO(MockDB):
    def setUp(self):
        # Before testing, grab the original passwords so they can be reset in tearDown
        super().setUp()
        self.cur.execute("SELECT employee_password FROM employees WHERE employee_username = 'DwightSchrute'")
        self.original_employee_password, = self.cur.fetchone()
        self.cur.execute("SELECT manager_password FROM managers WHERE manager_username = 'JoshPorter'")
        self.original_manager_password, = self.cur.fetchone()

    def test_reset_password_for_employee(self):
        """This will succeed because the new password is the same as what we updated it to be"""
        new_password = 'password'
        reset_password(new_password, 'DwightSchrute', True, productionDB=False)
        # Select the new password from the test DB
        self.cur.execute("SELECT employee_password FROM employees WHERE employee_username = 'DwightSchrute'")
        dao_updated_password, = self.cur.fetchone()
        self.assertEqual(new_password, dao_updated_password, 'The passwords do not match')

    def test_reset_password_for_manager(self):
        """This will succeed because the new password is the same as what we updated it to be"""
        new_password = 'password'
        reset_password(new_password, 'JoshPorter', False, productionDB=False)
        # Select the new password from the test DB
        self.cur.execute("SELECT manager_password FROM managers WHERE manager_username = 'JoshPorter'")
        dao_updated_password, = self.cur.fetchone()
        self.assertEqual(new_password, dao_updated_password, 'The passwords do not match')

    # Undo changes and reset tables back to normal
    def tearDown(self):
        self.cur.execute("UPDATE employees SET employee_password = '{}' WHERE employee_username = 'DwightSchrute'".format(self.original_employee_password))
        self.cur.execute("UPDATE managers SET manager_password = '{}' WHERE manager_username = 'JoshPorter'".format(self.original_manager_password))
        super().tearDown()