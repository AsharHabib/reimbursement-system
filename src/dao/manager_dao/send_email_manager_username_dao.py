# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Resend an email for the given manager's first and last names, find the manager username and email in the table
# where the first and last names match and return the username and email address
def send_email_manager_username(first_name, last_name, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        cur.execute("""SELECT manager_username, manager_email FROM managers WHERE
                            manager_first_name = %s AND manager_last_name = %s""", (first_name, last_name))
        info_logger.info('{} {} forgot their username, manager information retrieved'.format(first_name, last_name))
        return cur.fetchone()
    # Close the connection
    finally:
        conn.close()