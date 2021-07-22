# Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.manager_dao.get_reimbursements_under_manager_dao import get_reimbursements_under_manager


class TestGetReimbursementsUnderManagerDAO(MockDB):
    def test_all_reimbursements_under_manager_are_retrieved(self):
        """This test will succeed because the retrieved reimbursements match what was already there from MockDB's
        setUp, testing that both are equivalent"""
        self.dao_reimbursements_under_manager = get_reimbursements_under_manager(0, productionDB=False)
        self.assertCountEqual(self.test_reimbursements_under_manager, self.dao_reimbursements_under_manager, """
        The reimbursements are not exactly equal""")