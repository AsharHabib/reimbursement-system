# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Retrieve all the reimbursements for a certain employee's ID and all their data
def get_reimbursements_under_employee(employee_id, manager_id, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        sql_query = """SELECT reimbursement_id, amount, reason, datetime, status, 
            manager_message FROM reimbursements WHERE employee_id = %s ORDER BY datetime DESC"""
        cur.execute(sql_query, (employee_id,))
        reimbursements = cur.fetchall()
        info_logger.info("All reimbursements' data for employee #{} retrieved".format(employee_id))
        return reimbursements
    # Close the connection
    finally:
        conn.close()