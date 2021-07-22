# Import relevant DAO and call it in the service function
from src.dao.manager_dao import get_manager_first_last_names_dao

def get_manager_first_last_names():
    return get_manager_first_last_names_dao.get_manager_first_last_names()