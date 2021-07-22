# Import the get connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Return all usernames in both the managers and employees tables
def get_all_usernames(productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        cur.execute("SELECT manager_username FROM managers")
        manager_usernames, = zip(*cur.fetchall())
        cur.execute("SELECT employee_username FROM employees")
        employee_usernames, = zip(*cur.fetchall())
        info_logger.info('All usernames retrieved')
        return manager_usernames, employee_usernames
    # Close the connection
    finally:
        conn.close()