# Import relevant DAO and call it in the service function
from src.dao.manager_dao import get_employees_under_manager_dao

def get_employees_under_manager(manager_id, productionDB=True):
    return get_employees_under_manager_dao.get_employees_under_manager(manager_id, productionDB=productionDB)