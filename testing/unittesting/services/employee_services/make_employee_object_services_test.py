# Import relevant service method and the Employee data model class, and MockDB
from testing.unittesting.mock_db import MockDB
from unittest.mock import Mock
from src.models.employee import Employee
from src.services.employee_services.make_employee_object_services import make_employee_object
import src.dao.employee_dao.make_employee_object_dao as employee_dao

class TestMakeEmployeeObjectServices(MockDB):
    def setUp(self):
        #Inherit from super()'s setUp() and create a Mock object for the DAO to mock as returning
        super().setUp()
        employee_dao.make_employee_object = Mock(return_value=(1, 0, 'JimHalpert', 'jimhalpert', 'Jim', 'Halpert',
                                                               'Sales Rep', 'ashfrog96@gmail.com'))

    def test_service_returns_employee_object(self):
        """This will succeed because the service function creates a Manager object"""
        employee_object = make_employee_object('JimHalpert', productionDB=False)
        self.assertIsInstance(employee_object, Employee, "The service function did not return an Employee object")

    def tearDown(self):
        super().tearDown()