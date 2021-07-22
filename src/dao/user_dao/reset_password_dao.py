# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Reset the password after opening the link in the email, and after checking the new password
# and confirmed password inputs are equal, is_employee is a Boolean for if the account type is
# employee or not (i.e. manager), otherwise UPDATE the relevant tables with the new password
def reset_password(new_password, username, is_employee, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        if is_employee:
            cur.execute("""UPDATE employees SET employee_password = %s WHERE
             employee_username = %s""", (new_password, username))
            conn.commit()
        else:
            cur.execute("""UPDATE managers SET manager_password = %s WHERE
            manager_username = %s""", (new_password, username))
            conn.commit()
        info_logger.info('{} reset their password'.format(username))
    # Close the connection
    finally:
        conn.close()