# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Function for managers to update the status of the given reimbursement request's ID,
# must pass in all 3 IDs because the reimbursements table's primary key is all 3
# Manager message is required argument but it can be null when called
def update_status(reimbursement_id, employee_id, manager_id, new_status, manager_message, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        sql_query = """UPDATE reimbursements SET status = %s, manager_message = %s WHERE reimbursement_id = %s
                        AND employee_id = %s AND manager_id = %s"""
        cur.execute(sql_query, (new_status, manager_message, reimbursement_id, employee_id, manager_id))
        conn.commit()
        info_logger.info('Request(s) have been updated for manager #{}'.format(manager_id))
    # Close the connection
    finally:
        conn.close()