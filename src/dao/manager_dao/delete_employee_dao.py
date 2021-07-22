# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

#Function for a manager to delete a specific employee account, only employee ID is needed to
# uniquely identify an account and delete it
def delete_employee(employee_id, productionDB=True):
    try:
        # Establish the connection and cursor
        conn = get_connection(productionDB)
        cur = conn.cursor()
        # execute the DELETE query
        cur.execute("DELETE FROM employees WHERE employee_id = %s",
                    (str(employee_id),))
        info_logger.info("Employee #{} has been deleted".format(employee_id))
        conn.commit()
    finally:
        # Close the connection
        conn.close()