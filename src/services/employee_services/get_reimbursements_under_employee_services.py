# Import relevant DAO and call it in the service function
from src.dao.employee_dao import get_reimbursements_under_employee_dao
from src.models.reimbursement import Reimbursement
# Import info-level logger from logger.py
from src.logger import info_logger

def get_reimbursements_under_employee(employee_id, manager_id, first_name, last_name, productionDB=True):
    reimbursements_dict = {}
    returned_reimbursements = get_reimbursements_under_employee_dao.get_reimbursements_under_employee(employee_id, manager_id, productionDB=productionDB)
    key = 0
    for reimbursement in returned_reimbursements:
        reimbursement_id, amount, reason, date_time, status, manager_message = reimbursement
        date_time = date_time.strftime("%b %d, %Y, %I:%M:%S %p")
        reimbursement_object = Reimbursement(reimbursement_id, employee_id, amount, reason, date_time, status.capitalize(), first_name, last_name, manager_message)
        reimbursement_object.set_manager_id(manager_id)
        reimbursements_dict[key] = reimbursement_object
        key += 1
    info_logger.info('Reimbursements for Employee #{} been turned to dictionary of objects'.format(employee_id))
    return reimbursements_dict