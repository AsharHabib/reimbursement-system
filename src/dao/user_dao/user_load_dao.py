# Import the get connection function, session from flask
from src.utils.dbconfig import get_connection
from flask import session
# Import info-level logger from logger.py
from src.logger import info_logger

# DAO to return the model account type, depending on if a manager or employee logged in,
# because session['account_type'] is set whenever one of them logs in (auth.login_post_employee
# and auth.login_post_manager)
def user_load(user_id, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        # If session's account_type was Employee, get all data from employees table where the user_id
        # matches employee_id, fetch data and return
        if session['account_type'] == 'Employee':
            cur.execute('SELECT * FROM employees WHERE employee_id = {}'.format(user_id))
            info_logger.debug('Employee #{} information retrieved'.format(user_id))
            return cur.fetchone()
        # If session's account_type was Manager, get all data from managers table where the user_id
        # matches manager_id, fetch data and return
        elif session['account_type'] == 'Manager':
            cur.execute('SELECT * FROM managers WHERE manager_id = %s', str(user_id))
            info_logger.debug('Manager #{} information retrieved'.format(user_id))
            return cur.fetchone()
    # Close the connection
    finally:
        conn.close()