# Import relevant DAO, both data models, session from flask
from src.dao.user_dao import user_load_dao
from src.models.employee import Employee
from src.models.manager import Manager
from flask import session
# Import info-level logger from logger.py
from src.logger import info_logger

def user_load(user_id):
    # If session account type is Employee, get the employee data from the respective conditional
    # in the DAO, load that data in an Employee object, return it
    if session['account_type'] == 'Employee':
        employee_id, manager_id, employee_username, employee_password, employee_first_name, \
        employee_last_name, job_title, employee_email = user_load_dao.user_load(user_id)
        employee_object = Employee(employee_username, employee_password, employee_first_name, employee_last_name,
                                   job_title, employee_email)
        employee_object.set_employee_id(employee_id)
        employee_object.set_manager_id(manager_id)
        info_logger.debug('Employee #{} has logged in'.format(user_id))
        return employee_object
    # If session account type is a Manager, get the manager data from the respective conditional
    # in the DAO, load that data in a Manager object, return it
    elif session['account_type'] == 'Manager':
        manager_id, manager_username, manager_password, manager_first_name, manager_last_name, manager_email = user_load_dao.user_load(user_id)
        manager_object = Manager(manager_username, manager_password, manager_first_name, manager_last_name,
                                 manager_email)
        manager_object.set_manager_id(manager_id)
        info_logger.debug('Manager #{} has logged in'.format(user_id))
        return manager_object