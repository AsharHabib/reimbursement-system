# Import MockDB, relevant service function, Mock, and the DAO
from testing.unittesting.mock_db import MockDB
from unittest.mock import Mock
from src.services.employee_services.check_employee_exists_services import check_employee_exists
import src.dao.employee_dao.check_employee_exists_dao as check_dao

class TestCheckEmployeeExistsServices(MockDB):
    def setUp(self):
        #Inherit from super()'s setUp() and create a Mock object for the DAO to mock as returning
        super().setUp()
        all_names = [('DwightSchrute', 'dwightschrute'), ('JimHalpert', 'jimhalpert')]
        all_names = zip(*all_names)
        check_dao.check_employee_exists = Mock(return_value=all_names)

    def test_service_returns_true_if_valid_credentials(self):
        """Testing that if the username and password exist in the DB and they match, service will return True"""
        self.assertTrue(check_employee_exists('DwightSchrute', 'dwightschrute', productionDB=False),
                        'The service is not True')

    def test_service_returns_false_if_credentials_exist_but_dont_match(self):
        """Testing that if both credentials exist but they don't match each other, service returns False"""
        self.assertFalse(check_employee_exists('DwightSchrute', 'jimhalpert', productionDB=False), "The service isn't False")

    def test_service_returns_false_if_either_credential_doesnt_exist(self):
        """Testing that if either credential isn't valid, service returns False"""
        self.assertFalse(check_employee_exists('random', 'dwightschrute', productionDB=False), "The service isn't False")