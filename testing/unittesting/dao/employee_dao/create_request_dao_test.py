#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.employee_dao.create_request_dao import create_request
import datetime

class TestCreateRequestDAO(MockDB):
    def setUp(self):
        #Inherit from super()'s setUp, select count of all requests for an employee with employee_id = 1 and
        # manager_id = 0
        super().setUp()
        self.cur.execute('SELECT COUNT(*) FROM reimbursements WHERE employee_id = 1 AND manager_id = 0')
        data = self.cur.fetchone()
        self.old_number_of_requests = data[0]

    def test_new_request_created(self):
        """This will succeed because the number of requests increases by 1, tests if a new employee request is
                created"""
        create_request(1, 50, 'No reason', datetime.datetime.now(), 'pending', 0, 'Jim', 'Halpert', productionDB=False)
        self.cur.execute('SELECT COUNT(*) FROM reimbursements WHERE employee_id = 1 AND manager_id = 0')
        data = self.cur.fetchone()
        self.new_number_of_requests = data[0]
        self.assertEqual(self.new_number_of_requests - 1, self.old_number_of_requests, """The number of accounts did 
        not change""")

    # Undo the changes and set table back to normal
    def tearDown(self):
        self.cur.execute("DELETE FROM reimbursements WHERE reimbursement_id > 0")
        super().tearDown()