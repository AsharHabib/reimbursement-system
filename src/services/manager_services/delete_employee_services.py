# Import relevant DAO and call it in the service function
from src.dao.manager_dao import delete_employee_dao

def delete_employee(employee_id):
    delete_employee_dao.delete_employee(employee_id)