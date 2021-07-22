# Import relevant DAO and call it in the service function
from src.dao.user_dao import get_all_usernames_dao

def get_all_usernames():
    return get_all_usernames_dao.get_all_usernames()