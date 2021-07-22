# Import the connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Given the manager username, retrieve it's data from the managers table and return it
def make_manager_object(username, productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        cur.execute("SELECT * FROM managers WHERE manager_username = %s", (username,))
        info_logger.info('Manager object created for {}'.format(username))
        return cur.fetchone()
    # Close the connection
    finally:
        conn.close()
