# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Function for an employee to submit and create a reimbursement request, takes all the necessary parameters to occupy
# the reimbursements table with, generates reimbursement_id below
def create_request(employee_id, amount, reason, datetimenow, status,
                   manager_id, employee_first_name, employee_last_name, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        # To dynamically increase the reimbursement_ids (which are always continuous integers starting from 0, 1, 2,
        # ...,) take the count of all the reimbursements in the table where employee_id = employee_id, then get the
        # list of all the reimbursement_ids in the table, if these IDs are consecutive, then reimbursement_ids[-1] ==
        # original_amount - 1, else find the break in the IDs with a for loop and if-else
        cur.execute("SELECT COUNT(*) FROM reimbursements WHERE employee_id = {}".format(employee_id))
        original_amount, = cur.fetchone()
        cur.execute("SELECT reimbursement_id FROM reimbursements WHERE employee_id = {} ORDER BY reimbursement_id".format(employee_id))
        reimbursement_ids, = zip(*cur.fetchall())
        if reimbursement_ids[-1] == original_amount - 1:
            reimbursement_id = original_amount
        else:
            for part in range(original_amount):
                if reimbursement_ids[part] == part:
                    continue
                else:
                    reimbursement_id = part
                    break
        cur.execute("""INSERT INTO reimbursements VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (str(reimbursement_id), str(employee_id), str(amount), reason, datetimenow, status,
                            str(manager_id), employee_first_name, employee_last_name, 'N/A'))
        info_logger.info('New employee request created for {} {}'.format(employee_first_name, employee_last_name))
        conn.commit()
    # Close the connection
    finally:
        conn.close()