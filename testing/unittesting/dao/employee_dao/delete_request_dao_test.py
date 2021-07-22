#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.employee_dao.delete_request_dao import delete_request


class TestDeleteRequestDAO(MockDB):
    def setUp(self):
        #Inherit from super()'s setUp, select count of all requests for an employee with employee_id = 1
        super().setUp()
        self.cur.execute('SELECT COUNT(*) FROM reimbursements WHERE employee_id = 1')
        data = self.cur.fetchone()
        self.old_number_of_requests = data[0]

    def test_request_was_deleted(self):
        """This will succeed because the number of requests decreases by 1, tests if the specified request is
                deleted"""
        delete_request(0, 1, productionDB=False)
        self.cur.execute('SELECT COUNT(*) FROM reimbursements WHERE employee_id = 1')
        data = self.cur.fetchone()
        self.new_number_of_requests = data[0]
        self.assertEqual(self.new_number_of_requests + 1, self.old_number_of_requests, """The number of accounts did 
        not change""")

    # Undo the changes and set table back to normal
    def tearDown(self):
        self.cur.execute("INSERT INTO reimbursements VALUES (0,1,50,'Dwight threw my cellphone out the car.', '2021-06-24 13:10:35','pending',0,'Jim','Halpert',NULL)")
        super().tearDown()