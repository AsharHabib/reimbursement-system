# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Function to check the manager account exists with the user-given username and password. Does this by first getting
# tuples for usernames and password from the managers table
def check_manager_exists(productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        cur.execute('SELECT manager_username, manager_password FROM managers')
        managers = cur.fetchall()
        info_logger.info('All manager usernames, passwords retrieved')
        return zip(*managers)
    # Close the connection
    finally:
        conn.close()