# Import the get connection function, url_for for creating the links in the emails
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Send email for resetting the passwords, takes the account's username and account_type if the
# username is in employees or managers table, can't use session['account_type'] because
# this function gets used before an account is logged in ('Forgot password?' link on the login page)
def send_email_password_reset(username, account_type, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        # Import the mail, serializer objects, and Message class from src.app
        from src.app import mail, serializer, Message
        info_logger.info('{} attempted to reset password, the email address was retrieved'.format(username))
        # If the account_type is 'manager', find the manager email from managers table where username equals
        # manager_username in the table,
        if account_type == 'manager':
            sql_query = "SELECT manager_email FROM managers WHERE manager_username = %s"
            cur.execute(sql_query, (username,))
            manager_email, = cur.fetchone()
            return manager_email
        # Similar to above but account_type is 'employee' and we search through the employees table
        # for the email address this time
        elif account_type == 'employee':
            sql_query = "SELECT employee_email FROM employees WHERE employee_username = %s"
            cur.execute(sql_query, (username,))
            employee_email, = cur.fetchone()
            return employee_email
    # Close the connection
    finally:
        conn.close()