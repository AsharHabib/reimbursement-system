# Import get_connection function
from src.utils.dbconfig import get_connection
# Import info-level logger from logger.py
from src.logger import info_logger

# Get the first and last names of all the managers
def get_manager_first_last_names(productionDB=True):
    try:
        conn = get_connection(productionDB)
        cur = conn.cursor()
        cur.execute("SELECT manager_first_name, manager_last_name FROM managers ORDER BY manager_id")
        info_logger.info('All manager first and last names retrieved')
        return zip(*cur.fetchall())
    # Close the connection
    finally:
        conn.close()