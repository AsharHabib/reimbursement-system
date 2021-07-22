# Import relevant DAO and call it in the service function
from src.dao.manager_dao import update_status_dao

def update_status(reimbursement_id, employee_id, manager_id, new_status, manager_message):
    update_status_dao.update_status(reimbursement_id, employee_id, manager_id, new_status, manager_message)