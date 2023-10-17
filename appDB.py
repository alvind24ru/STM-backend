import logging
import sqlite3


def init_database(dbname):
    try:
        conn = sqlite3.connect(dbname, check_same_thread=False)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
           userid INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT UNIQUE);
        """)
        cur.execute("""CREATE TABLE IF NOT EXISTS tasks(
           taskid INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT,
           title TEXT,
           description TEXT, 
           done BOOLEAN,
           FOREIGN KEY(username) REFERENCES users(username));
        """)
        conn.commit()
        conn.close()
    except Exception:
        logging.critical("Исключение при создании БД", exc_info=True)


def drop_all(dbname):
    try:
        conn = sqlite3.connect(dbname, check_same_thread=False)
        cur = conn.cursor()
        cur.execute("""DELETE FROM users WHERE type='table';""")
        conn.commit()
        conn.close()
    except Exception:
        logging.critical("Исключение при создании БД", exc_info=True)
