#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.manager_dao.delete_employee_dao import delete_employee


class TestDeleteEmployeeDAO(MockDB):
    def setUp(self):
        #Inherit from super()'s setUp, select count of all employees for a manager with id = 1
        super().setUp()
        self.cur.execute('SELECT COUNT(*) FROM employees WHERE manager_id = 1')
        data = self.cur.fetchone()
        self.old_number_of_employees = data[0]

    def test_employee_was_deleted(self):
        """This will succeed because the number of employees decreases by 1, tests if the specified employee is
                        deleted"""
        delete_employee(2, productionDB=False)
        self.cur.execute('SELECT COUNT(*) FROM employees WHERE manager_id = 1')
        data = self.cur.fetchone()
        self.new_number_of_employees = data[0]
        self.assertEqual(self.new_number_of_employees + 1, self.old_number_of_employees, """The number of accounts did 
                not change""")

    # Undo the changes and set table back to normal
    def tearDown(self):
        self.cur.execute("INSERT INTO employees VALUES (2, 1, 'AndyBernard', 'andybernard', 'Andy', 'Bernard', 'Sales Rep', 'ashfrog96@gmail.com')")
        self.cur.execute("INSERT INTO reimbursements VALUES (0,2,50,'I punched the wall','2021-06-24 08:10:35','pending',1,'Andy','Bernard','N/A','Sales Rep')")
        super().tearDown()