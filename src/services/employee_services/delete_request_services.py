# Import relevant DAO and call it in the service function
from src.dao.employee_dao import delete_request_dao

def delete_request(reimbursement_id, employee_id):
    delete_request_dao.delete_request(reimbursement_id, employee_id)