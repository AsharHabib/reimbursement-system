# Import MockDB, relevant service function, Mock, and the DAO
from testing.unittesting.mock_db import MockDB
import src.dao.manager_dao.check_manager_exists_dao as check_dao
from unittest.mock import Mock
from src.services.manager_services.check_manager_exists_services import check_manager_exists

class TestCheckManagerExistsServices(MockDB):
    def setUp(self):
        #Inherit from super()'s setUp() and create a Mock object for the DAO to mock as returning
        super().setUp()
        all_names = [('JoshPorter', 'joshporter'), ('MichaelScott', 'michaelscott')]
        all_names = zip(*all_names)
        check_dao.check_manager_exists = Mock(return_value=all_names)

    def test_service_returns_true_if_valid_credentials(self):
        """Testing that if the username and password exist in the DB and they match, service will return True"""
        self.assertTrue(check_manager_exists('JoshPorter', 'joshporter', productionDB=False), "The service isn't True")

    def test_service_returns_false_if_credentials_exist_but_dont_match(self):
        """Testing that if both credentials exist but they don't match each other, service returns False"""
        self.assertFalse(check_manager_exists('JoshPorter', 'michaelscott', productionDB=False), "The service isn't False")

    def test_service_returns_false_if_either_credential_doesnt_exist(self):
        """Testing that if either credential isn't valid, service returns False"""
        self.assertFalse(check_manager_exists('random', 'joshporter', productionDB=False), "The service isn't False")