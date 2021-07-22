# Import the get connection function, flash from flask
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Function to check the employee account exists with the user-given username and password. Does this by first getting
# tuples for usernames and password from the employees table
def check_employee_exists(productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        cur.execute('SELECT employee_username, employee_password FROM employees')
        employees = cur.fetchall()
        info_logger.info('All employee usernames, passwords retrieved')
        return zip(*employees)
    # Close the connection
    finally:
        conn.close()