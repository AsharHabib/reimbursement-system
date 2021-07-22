# Need the model to override UserMixin, to inherit it's methods/properties
from flask_login import UserMixin
# Data model for employees
class Employee(UserMixin):
    # Initial constructor
    def __init__(self, _username, _password, _first_name, _last_name, _job_title, _email):
        self._username = _username
        self._password = _password
        self._first_name = _first_name
        self._last_name = _last_name
        self._job_title = _job_title
        self._email = _email

    # Setter getters for employee, manager IDs
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def get_employee_id(self):
        return self._employee_id

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

    def get_manager_id(self):
        return self._manager_id

    # Override methods from UserMixin
    def get_id(self):
        return self._employee_id

    def get_urole(self):
        return 'Employee'

    def is_authenticated(self):
        return True