# Import unittest to create the TestCases
import unittest
# Import get_connection to establish connection with testing database
from src.utils.dbconfig import get_connection

class MockDB(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # Establish connection and cursor
        cls.conn = get_connection(productionDB=False)
        cls.cur = cls.conn.cursor()
        # Retrieve all managers from test database (only 2 managers in there)
        cls.cur.execute("SELECT * FROM managers ORDER BY manager_id")
        cls.list_of_test_managers = cls.cur.fetchall()
        # Retrieve all employees from test database (only 2 employees in there)
        cls.cur.execute("SELECT * FROM employees ORDER BY manager_id, employee_id")
        cls.list_of_test_employees = cls.cur.fetchall()
        # Retrieve one email address from managers and employees, used for testing send_email_password_reset
        cls.cur.execute("SELECT manager_email FROM managers WHERE manager_id = 0")
        cls.test_manager_email, = cls.cur.fetchone()
        cls.cur.execute('SELECT employee_email FROM employees WHERE employee_id = 1')
        cls.test_employee_email, = cls.cur.fetchone()
        # Retrieve all usernames from both tables, used for testing get_all_usernames
        cls.cur.execute("SELECT manager_username FROM managers")
        cls.test_manager_usernames, = zip(*cls.cur.fetchall())
        cls.cur.execute("SELECT employee_username FROM employees")
        cls.test_employee_usernames, = zip(*cls.cur.fetchall())
        # Retrieve a username and email from the managers table, used for testing send_email_manager_username
        cls.cur.execute("""SELECT manager_username, manager_email FROM managers WHERE
                            manager_first_name = 'Michael' AND manager_last_name = 'Scott'""")
        cls.test_manager_email_username = cls.cur.fetchone()
        # Retrieve all manager data for username = 'JoshPorter', used for testing make_manager_object
        cls.cur.execute("SELECT * FROM managers WHERE manager_username = 'JoshPorter'")
        cls.test_manager_object = cls.cur.fetchone()
        # Retrieve all reimbursements (and data) under a manager, used for testing get_reimbursements_under_manager
        cls.cur.execute("""SELECT reimbursement_id, employee_id, amount, reason, datetime, 
    status, employee_first_name, employee_last_name, job_title FROM reimbursements WHERE manager_id = 0 ORDER BY datetime DESC""")
        cls.test_reimbursements_under_manager = cls.cur.fetchall()
        # Retrieve first and last names for all managers, used for testing get_manager_first_last_names
        cls.cur.execute("SELECT manager_first_name, manager_last_name FROM managers ORDER BY manager_id")
        data = cls.cur.fetchall()
        # Zip to mirror the functionality in the DAO
        cls.test_first_last_manager_names = zip(*data)
        # Retrieve all employees under manager #0, used for testing get_employees_under_manager
        cls.cur.execute("""SELECT employee_id, employee_first_name, employee_last_name, job_title FROM employees
                WHERE manager_id = 0""")
        # Zip to mirror the functionality in the DAO
        data = cls.cur.fetchall()
        cls.test_employees_under_manager = zip(*data)
        # Retrieve usernames and passwords for all managers, used for testing check_manager_exists
        cls.cur.execute('SELECT manager_username, manager_password FROM managers')
        # Zip to mirror the functionality in the DAO
        data = cls.cur.fetchall()
        cls.test_check_manager_exists = zip(*data)

        # Retrieve a username and password from the employees table, used for testing send_email_employee_username
        cls.cur.execute("""SELECT employee_username, employee_email FROM employees WHERE
                                employee_first_name = 'Dwight' AND employee_last_name = 'Schrute'""")
        cls.test_employee_email_username = cls.cur.fetchone()
        # Retrieve employee data with a given username, used for testing make_employee_object
        cls.cur.execute("""SELECT * FROM employees WHERE employee_username = 'JimHalpert'""")
        cls.test_employee_object = cls.cur.fetchone()
        # Retrieve all reimbursements under an employee, used for testing get_reimbursements_under_employee
        cls.cur.execute("""SELECT reimbursement_id, amount, reason, datetime, status, 
            manager_message FROM reimbursements WHERE employee_id = 0 ORDER BY datetime DESC""")
        cls.test_reimbursements_under_employee = cls.cur.fetchall()
        # Retrieve first and last names for all employees, used for testing get_employee_first_last_names
        cls.cur.execute("SELECT employee_first_name, employee_last_name FROM employees ORDER BY employee_id")
        # Zip to mirror functionality in the DAO
        data = cls.cur.fetchall()
        cls.test_first_last_employee_names = zip(*data)
        # Retrieve usernames and passwords for all employees, used for testing check_employee_exists
        cls.cur.execute('SELECT employee_username, employee_password FROM employees')
        # Zip to mirror functionality in the DAO
        data = cls.cur.fetchall()
        cls.test_check_employee_exists = zip(*data)


    @classmethod
    def tearDown(cls):
        # Close connections after each test
        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()
