import sqlite3


def user_is_available(userid=None, username=None):
    """Отдает True если пользователь есть в БД. Ищет пользователя по имени ИЛИ id"""
    global res
    try:
        if userid:
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""SELECT * FROM users WHERE userid = {userid}""")
            res = cur.fetchall()
            conn.close()
        elif username:
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""SELECT * FROM users WHERE username = '{username}'""")
            res = cur.fetchall()
            conn.close()
        if res:
            return True
        else:
            return False
    except Exception:
        pass


def task_is_available(taskid):
    conn = sqlite3.connect('STM.db', check_same_thread=False)
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM tasks WHERE taskid = {taskid}""")
    res = cur.fetchall()
    conn.close()
    if res:
        return True
    else:
        return False
