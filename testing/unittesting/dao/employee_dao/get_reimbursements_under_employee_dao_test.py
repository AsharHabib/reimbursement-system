# Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.employee_dao.get_reimbursements_under_employee_dao import get_reimbursements_under_employee

class TestGetReimbursementsUnderEmployeeDAO(MockDB):
    def test_all_reimbursements_under_employee_are_retrieved(self):
        """This test will succeed because the retrieved reimbursements match what was already there from MockDB's
        setUp, testing that both are equivalent"""
        self.dao_reimbursements_under_employee = get_reimbursements_under_employee(0, 0, productionDB=False)
        self.assertCountEqual(self.test_reimbursements_under_employee, self.dao_reimbursements_under_employee, """The 
        reimbursements are not exactly equal""")