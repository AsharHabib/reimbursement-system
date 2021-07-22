# Import the get connection function
import os
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Create a new employee account, only accessible for managers, arguments are necessary information
# for an employee data entry in the employee tables, and employee_id is found in the function
def create_employee_account(manager_id, first_name, last_name, username, password, job_title, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        # To dynamically increase the employee_ids (which are always continuous integers starting from
        # 0, 1, 2, ...,) take the count of all the employees in the table, then get the list of all employee ids
        # If the IDs are consecutive, then employee_ids[-1] == original_amount - 1, else find the break in IDs
        # using a for loop and if-else statement
        cur.execute('SELECT COUNT(*) FROM employees')
        count = cur.fetchone()
        original_amount = count[0]
        cur.execute("SELECT employee_id FROM employees ORDER BY employee_id")
        employee_ids, = zip(*cur.fetchall())
        if employee_ids[-1] == original_amount - 1:
            employee_id = original_amount
        else:
            for part in range(original_amount):
                if employee_ids[part] == part:
                    continue
                else:
                    employee_id = part
                    break
        cur.execute("""INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
                    , (str(employee_id), manager_id, username, password, first_name, last_name, job_title,
                       os.environ['MAIL_USERNAME']))
        conn.commit()
        info_logger.info("New empmloyee account created")
    # Close the connection
    finally:
        conn.close()