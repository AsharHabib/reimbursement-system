# Import relevant DAO and call it in the service function
from src.dao.manager_dao import employees_under_manager_dao

def employees_under_manager(manager_username):
    return employees_under_manager_dao.employees_under_manager(manager_username)