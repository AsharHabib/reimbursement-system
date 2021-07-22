# Import relevant DAO and call it in the service function, and Manager data model class
from src.dao.manager_dao import make_manager_object_dao
from src.models.manager import Manager
# Import info-level logger from logger.py
from src.logger import info_logger

# Get the manager data from the DAO, load the data in a Manager object and return that
def make_manager_object(username, productionDB=True):
    manager_id, manager_username, manager_password, manager_first_name, \
    manager_last_name, manager_email = make_manager_object_dao.make_manager_object(username, productionDB)
    manager = Manager(manager_username, manager_password, manager_first_name, manager_last_name, manager_email)
    manager.set_manager_id(manager_id)
    info_logger.info('Manager object created for {}'.format(username))
    return manager