# Import relevant service method and the Manager data model class, and MockDB
from testing.unittesting.mock_db import MockDB
from src.models.manager import Manager
import src.dao.manager_dao.make_manager_object_dao as manager_dao
from unittest.mock import Mock
from src.services.manager_services.make_manager_object_services import make_manager_object

class TestMakeManagerObjectServices(MockDB):
    def setUp(self):
        #Inherit from super()'s setUp() and create a Mock object for the DAO to mock as returning
        super().setUp()
        manager_dao.make_manager_object = Mock(return_value=(0, 'MichaelScott', 'michaelscott',
                                            'Michael', 'Scott', 'ashfrog96@gmail.com'))


    def test_service_returns_manager_object(self):
        """This will succeed because the service function creates a Manager object"""
        manager_object = make_manager_object('MichaelScott', productionDB=False)
        self.assertIsInstance(manager_object, Manager, "The service function did not return a Manager object")

    def tearDown(self):
        super().tearDown()