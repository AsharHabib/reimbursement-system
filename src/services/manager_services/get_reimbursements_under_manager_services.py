# Import relevant DAO and call it in the service function
from src.dao.manager_dao import get_reimbursements_under_manager_dao
from src.models.reimbursement import Reimbursement
# Import info-level logger from logger.py
from src.logger import info_logger

def get_reimbursements_under_manager(manager_id, productionDB=True):
    reimbursements_dict = {}
    returned_reimbursements = get_reimbursements_under_manager_dao.get_reimbursements_under_manager(manager_id, productionDB=productionDB)
    key = 0
    for reimbursement in returned_reimbursements:
        reimbursement_id, employee_id, amount, reason, date_time, status, first_name, last_name, job_title = reimbursement
        date_time = date_time.strftime("%b %d, %Y, %I:%M:%S %p")
        reimbursement_object = Reimbursement(reimbursement_id, employee_id, amount, reason, date_time, status.capitalize(), first_name, last_name, job_title=job_title)
        reimbursement_object.set_manager_id(manager_id)
        reimbursements_dict[key] = reimbursement_object
        key += 1
    info_logger.info('Reimbursements for Manager #{} turned into dictionary of objects'.format(manager_id))
    return reimbursements_dict