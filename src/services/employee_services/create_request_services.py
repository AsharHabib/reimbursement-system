# Import relevant DAO and call it in the service function
from src.dao.employee_dao import create_request_dao

def create_request(employee_id, amount, reason, datetimenow, status, manager_id, employee_first_name, employee_last_name):
    create_request_dao.create_request(employee_id, amount, reason, datetimenow, status, manager_id, employee_first_name, employee_last_name)