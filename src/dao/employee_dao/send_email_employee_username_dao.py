# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Send email if an employee forgets their username, grab the username and email address from
# the employees table where first and last names match, return the username and email address
def send_email_employee_username(first_name, last_name, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        cur.execute("""SELECT employee_username, employee_email FROM employees WHERE
                                employee_first_name = %s AND employee_last_name = %s""", (first_name, last_name))
        info_logger.info('Employee username, email for {} {} retrieved'.format(first_name, last_name))
        return cur.fetchone()
    # Close the connection
    finally:
        conn.close()