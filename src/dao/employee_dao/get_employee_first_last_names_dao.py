# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Get the first and last names for all the employees
def get_employee_first_last_names(productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        cur.execute("SELECT employee_first_name, employee_last_name FROM employees ORDER BY employee_id")
        info_logger.info('All employee first, last names retrieved')
        return zip(*cur.fetchall())
    # Close the connection
    finally:
        conn.close()