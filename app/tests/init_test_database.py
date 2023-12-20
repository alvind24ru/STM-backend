import logging
import sqlite3


def init_test_database(dbname):
    """Создает тестовую базу данных с тестовыми значениями"""
    try:
        conn = sqlite3.connect(dbname, check_same_thread=False)
        cur = conn.cursor()
        cur.executescript("""CREATE TABLE IF NOT EXISTS users(
           userid INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT UNIQUE);
           CREATE TABLE IF NOT EXISTS tasks(
           taskid INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT,
           title TEXT,
           description TEXT,
           done BOOLEAN,
           FOREIGN KEY(username) REFERENCES users(username));
           INSERT INTO users(username) VALUES ('test_user');
           INSERT INTO users(username) VALUES ('test_user1');
           INSERT INTO users(username) VALUES ('test_user2');
           INSERT INTO tasks (username, title, description, done)
           VALUES ('test_user', 'test_title', 'test_description', 'False');
           INSERT INTO tasks (username, title, description, done)
           VALUES ('test_user', 'test_title', 'test_description', 'False');
           INSERT INTO tasks (username, title, description, done)
           VALUES ('test_user1', 'test_title', 'test_description', 'False');
        """)
        conn.commit()
        conn.close()
    except Exception:
        logging.critical("Исключение при создании БД", exc_info=True)
