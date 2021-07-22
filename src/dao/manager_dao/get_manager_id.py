from src.utils.dbconfig import get_connection

def get_manager_id(manager_username):
    conn = get_connection()
    cur = conn.cursor()
    sql_query = """SELECT manager_id FROM managers WHERE manager_username = %s"""
    cur.execute(sql_query, (manager_username,))
    manager_id = cur.fetchone()
    return manager_id[0]