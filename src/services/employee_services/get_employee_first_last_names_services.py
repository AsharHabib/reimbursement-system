# Import relevant DAO and call it in the service function
from src.dao.employee_dao import get_employee_first_last_names_dao

def get_employee_first_last_names():
    return get_employee_first_last_names_dao.get_employee_first_last_names()