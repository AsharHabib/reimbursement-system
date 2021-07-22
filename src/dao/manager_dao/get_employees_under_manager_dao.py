# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Get all information for employees under a manager with the manager ID passed in
def get_employees_under_manager(manager_id, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        sql_query = """SELECT employee_id, employee_first_name, employee_last_name, job_title FROM employees
                WHERE manager_id = %s ORDER BY employee_id"""
        cur.execute(sql_query, (manager_id,))
        data = cur.fetchall()
        info_logger.info("Employee data under Manager #{} retrieved".format(manager_id))
        return zip(*data)
    # Close the connection
    finally:
        conn.close()