# Import relevant DAO and call it in the service function, and Employee data model class
from src.dao.employee_dao import make_employee_object_dao
from src.models.employee import Employee
# Import info-level logger from logger.py
from src.logger import info_logger

# Gets data from the DAO, creates an Employee object with the data, returns the object
def make_employee_object(username, productionDB=True):
    employee_id, manager_id, employee_username, employee_password, employee_first_name, \
    employee_last_name, job_title, employee_email = make_employee_object_dao.make_employee_object(username, productionDB)
    employee = Employee(employee_username, employee_password, employee_first_name, employee_last_name, job_title,
                         employee_email)
    employee.set_employee_id(employee_id)
    employee.set_manager_id(manager_id)
    info_logger.info('Employee object for {} has been created'.format(username))
    return employee