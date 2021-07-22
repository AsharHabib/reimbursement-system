#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.manager_dao.update_status_dao import update_status

class TestUpdateStatusDAO(MockDB):
    def setUp(self):
        # Before testing, grab the original status so they can be used to reset DB in tearDown
        super().setUp()
        # There's only 1 reimbursement where employee_id = 1 in the test DB
        self.cur.execute("SELECT status FROM reimbursements WHERE employee_id = 1")
        self.dao_original_status, = self.cur.fetchone()

    def test_status_was_updated(self):
        """This will succeed because the updated status is what we expected it to be"""
        new_status = 'accepted'
        update_status(0, 1, 0, new_status, None, productionDB=False)
        # Select the new password from the test DB
        self.cur.execute("SELECT status FROM reimbursements WHERE employee_id = 1")
        self.dao_updated_status, = self.cur.fetchone()
        self.assertEqual(new_status, self.dao_updated_status, 'The statuses do not match')

    def tearDown(self):
        self.cur.execute("UPDATE reimbursements SET status = '{}' WHERE employee_id = 1".format(self.dao_original_status))
        super().tearDown()