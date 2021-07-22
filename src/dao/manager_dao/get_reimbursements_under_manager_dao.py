from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Get all reimburesements under a manager
def get_reimbursements_under_manager(manager_id, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        sql_query = """SELECT reimbursement_id, employee_id, amount, reason, datetime, 
            status, employee_first_name, employee_last_name, job_title FROM reimbursements WHERE manager_id = %s ORDER BY datetime DESC"""
        cur.execute(sql_query, (manager_id,))
        reimbursements = cur.fetchall()
        info_logger.info('All reimbursment data under Manager #{} retrieved'.format(manager_id))
        return reimbursements
    finally:
        conn.close()