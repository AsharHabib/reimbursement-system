from src.utils.dbconfig import cur
from src.dao.manager_dao.get_employees_under_manager_dao import get_employees_under_manager

def employees_under_manager(manager_id):
    sql_query = """SELECT manager_id, manager_first_name, manager_last_name FROM managers
     WHERE manager_id = %s"""
    cur.execute(sql_query, (manager_id,))
    manager_id, manager_first_name, manager_last_name = cur.fetchone()
    employee_ids, employee_first_names, employee_last_names, job_titles = get_employees_under_manager(manager_id)
    return (employee_ids, employee_first_names, employee_last_names, job_titles)