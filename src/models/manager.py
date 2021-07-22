# Need the model to override UserMixin, to inherit it's methods/properties
from flask_login import UserMixin
# Data model for managers
class Manager(UserMixin):
    # Initial constructor
    def __init__(self, _username, _password, _first_name, _last_name, _email):
        self._username = _username
        self._password = _password
        self._first_name = _first_name
        self._last_name = _last_name
        self._email = _email

    # Setter getter methods for the ID
    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

    def get_manager_id(self):
        return self._manager_id

    # Overriding methods from UserMixin
    def get_id(self):
        return self._manager_id

    def get_urole(self):
        return 'Manager'

    def is_authenticated(self):
        return True