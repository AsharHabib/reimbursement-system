# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

#Function for an employee to delete a specific request, only reimbursement and employee ID are needed to
# uniquely identify a request and delete it
def delete_request(reimbursement_id, employee_id, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        # execute the DELETE query
        cur.execute("DELETE FROM reimbursements WHERE reimbursement_id = %s AND employee_id = %s",
                    (str(reimbursement_id), str(employee_id)))
        info_logger.info('Reimbursement for employee #{} deleted'.format(employee_id))
        conn.commit()
    finally:
        conn.close()