#Import MockDB, relevant DAO function
from testing.unittesting.mock_db import MockDB
from src.dao.manager_dao.make_manager_object_dao import make_manager_object

class TestMakeManagerObjectDAO(MockDB):
    def test_dao_retrieves_all_manager_data(self):
        """This will succeed because both data sets match, testing that we do retrieve all manager data given his/her
        username"""
        self.dao_manager_object = make_manager_object('JoshPorter', productionDB=False)
        self.assertEqual(self.test_manager_object, self.dao_manager_object, 'The data sets were not equal')