# Import relevant DAO and call it in the service function
from src.dao.user_dao import reset_password_dao


def reset_password(new_password, username, is_employee):
    reset_password_dao.reset_password(new_password, username, is_employee)