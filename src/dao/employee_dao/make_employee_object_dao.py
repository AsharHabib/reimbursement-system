# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Given the employee username, retrieve it's data from the employees table and return that
def make_employee_object(username, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees WHERE employee_username = %s", (username,))
        info_logger.info('All employee data for {} retrieved'.format(username))
        return cur.fetchone()
    # Close the connection
    finally:
        conn.close()