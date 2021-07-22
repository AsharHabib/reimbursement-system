# Import relevant DAO and call it in the service function
from flask import flash

from src.dao.employee_dao import check_employee_exists_dao
# Import info-level and warning-level loggers from logger.py
from src.logger import info_logger, my_logger

# Gets the employee usernames and passwords from the DAO, compares the indices for username and password in the
# respective tuples, if they are not equal then that means both the username and password exist in the table but they
# don't match, ValueError occurs if the username or password don't exist in the table at all
def check_employee_exists(username, password, productionDB=True):
    usernames, passwords = check_employee_exists_dao.check_employee_exists(productionDB)
    try:
        if usernames.index(username) == passwords.index(password):
            info_logger.info("Username and password match")
            return True
        else:
            my_logger.warning('Username and password do not match')
            return False
    except ValueError:
        flash('Please check your login details and try again.')
        my_logger.error("Either username or password do not exist")
        return False