# Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.manager_dao.get_manager_first_last_names_dao import get_manager_first_last_names

class TestGetManagerFirstLastNamesDAO(MockDB):
    def test_all_first_last_manager_names_returned(self):
        """This will succeed because the DAO retrieves the expected results that were made in MockDB's setUp(), tests
        that the first and last names for all managers are returned"""
        self.dao_first_last_manager_names = get_manager_first_last_names(productionDB=False)
        self.assertCountEqual(self.test_first_last_manager_names, self.dao_first_last_manager_names, """The arguments
        are not exactly equal""")