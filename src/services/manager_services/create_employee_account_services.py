# Import relevant DAO and call it in the service function
from src.dao.manager_dao import create_employee_account_dao

def create_employee_account(manager_id, first_name, last_name, username, password, job_title):
    create_employee_account_dao.create_employee_account(manager_id, first_name, last_name, username, password, job_title)