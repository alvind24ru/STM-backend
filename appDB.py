import sqlite3


def init_database(dbname):
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
