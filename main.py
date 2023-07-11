import logging
from flask import Flask, json, request
import sqlite3
import scripts




with open('apidoc.json') as file:
    data = json.load(file)

VERSION = 'v' + data['version']

logging.basicConfig(level=logging.INFO, filename="py_log.txt",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("___________________________________Сервер начал работу___________________________________")
try:
    conn = sqlite3.connect('STM.db', check_same_thread=False)
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

app = Flask(__name__)


@app.route(f'/{VERSION}/create/user', methods=['POST'])
def create_user():
    logging.info("Получен запрос создания пользователя")
    if 'username' in request.args:
        try:
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            username = request.args['username']
            cur.execute(f"""INSERT INTO users(username) 
            VALUES('{username}');""")
            conn.commit()
            cur.execute(f"SELECT userid, username FROM users WHERE username='{username}'")
            created_user = scripts.list_to_json(cur=cur, data=cur.fetchall())
            conn.close()
        except sqlite3.IntegrityError:
            logging.error("Указанное имя пользователя уже имеется", exc_info=True)
            return 'UsernameError'
        except Exception:
            logging.critical("Исключение при запросе на добавление пользователя", exc_info=True)
        else:
            return created_user
    else:
        logging.info("Не все необходимые аргументы найдены")
        return "InvalidArguments"


@app.route(f'/{VERSION}/get/user', methods=['GET'])
def get_user():
    logging.info("Получен запрос на получение пользователя")
    if 'username' in request.args:
        try:
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            username = request.args['username']
            cur.execute(f"SELECT userid, username FROM users WHERE username='{username}'")
            result = scripts.list_to_json(cur=cur, data=cur.fetchall())
            conn.close()
        except Exception:
            logging.critical(f"Исключение при запросе получения пользователя", exc_info=True)
        else:
            return result

@app.route(f'/{VERSION}/update/user', methods=['POST'])
def change_username():
    pass

@app.route(f'/{VERSION}/delete/user', methods=['POST'])
def delete_user():
    pass


# get all users
@app.route(f'/{VERSION}/get/all_users', methods=['GET'])
def get_all_users():
    logging.info("Получен запрос списка пользователей")
    try:
        conn = sqlite3.connect('STM.db', check_same_thread=False)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users;")
        result = scripts.list_to_json(cur, cur.fetchall())
        conn.close()
        logging.info("Список пользователей успешно предоставлен")
        return result, 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception:
        logging.critical("Исключение при запросе списка пользователей", exc_info=True)


@app.route(f'/{VERSION}/create/task', methods=['POST', 'GET'])
def create_task():
    logging.info("Получен запрос на добавление задачи")
    if 'username' in request.args and 'title' in request.args and 'description' in request.args and 'done' in request.args:
        try:
            username = request.args['username']
            title = request.args['title']
            description = request.args['description']
            done = request.args['done']
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute("""SELECT username FROM users""")
            username_list = cur.fetchall()
            for i in range(len(username_list)):
                if username == username_list[i][0]:
                    cur.execute(f"""INSERT INTO tasks(username, title, description, done) 
                        VALUES('{username}', '{title}', '{description}', '{done}');""")
                    conn.commit()
                    conn.close()
                    logging.info("Добавлена задача")
                    return "Task added!"
            else:
                logging.info("данный username не найден для добавления задачи")
                return f"User {username} is not found!"
        except Exception as e:
            logging.critical("Исключение при добавлении задачи", exc_info=True)
            return str(e)
    else:
        logging.info("Не все необходимые аргументы найдены")
        return "Invalid argument"


@app.route('/todo/api/v1.0/get_tasks', methods=['GET'])
def get_all_user_tasks():
    logging.info("Получен запрос на получение списка задач")
    if 'userid' in request.args:
        try:
            userid = request.args['userid']
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""SELECT username FROM users WHERE userid == {userid}""")
            username = cur.fetchone()[0]
            cur.execute(f"""SELECT * FROM tasks WHERE username == '{username}'""")
            user_tasks_list = scripts.list_to_json(cur, cur.fetchall())
            logging.info(f"Список задач пользователя {username} предоставлен")
            conn.commit()
            conn.close()
            return user_tasks_list, {'Content-Type': 'application/json; charset=utf-8'}
        except Exception as e:
            logging.critical("Исключение при попытке получения задач", exc_info=True)
            return str(e)
    else:
        logging.info("Не все необходимые аргументы найдены")
        return "Invalid argument"

@app.route('/todo/api/v1.0/get_task', methods=['GET'])
def get_task():
    pass


@app.route('/todo/api/v1.0/update_tasks', methods=['GET'])
def update_tasks():
    if 'taskid' in request.args:
        try:
            title_status = 0
            description_status = 0
            taskid = request.args['taskid']
            if 'title' in request.args:
                title = request.args['title']
                conn = sqlite3.connect('STM.db', check_same_thread=False)
                cur = conn.cursor()
                cur.execute(f"""UPDATE tasks SET title = '{title}' WHERE taskid = {taskid}""")
                logging.info(f"Title has updated")
                conn.commit()
                conn.close()
                title_status = 1
            if 'description' in request.args:
                description = request.args['description']
                conn = sqlite3.connect('STM.db', check_same_thread=False)
                cur = conn.cursor()
                cur.execute(f"""UPDATE tasks SET description = '{description}' WHERE taskid = {taskid}""")
                logging.info(f"description has updated")
                conn.commit()
                conn.close()
                description_status = 1
            if description_status == 1 and title_status == 0:
                return 'descriprion has change'
            if title_status == 1 and description_status == 0:
                return 'title has change'
            if title_status == 1 and description_status == 1:
                return 'title and descriprion has change'
        except Exception as e:
            logging.critical("Исключение при попытке изменения задачи", exc_info=True)
            return str(e)

    else:
        logging.info("Не все необходимые аргументы найдены")
        return "Invalid argument"


@app.route('/todo/api/v1.0/delete_tasks', methods=['GET'])
def delete_tasks():
    logging.info("Получен запрос на удаление задачи")
    if 'taskid' in request.args:
        try:
            taskid = request.args['taskid']
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute(
                f"""DELETE FROM tasks WHERE taskid = {taskid}""")  # TODO не возвращает ошибку даже если записи с таким ID нет в таблице
            logging.info(f"Задача с ID {taskid} удалена")
            print(f"Задача с ID {taskid} удалена")
            conn.commit()
            conn.close()
            return 'OK'
        except Exception as e:
            logging.critical("Исключение при попытке удаления задачи", exc_info=True)
            return str(e)
    else:
        logging.info("Не все необходимые аргументы найдены")
        return "Invalid argument"

def test():
    return 'True'
# @app.route('/todo/api/v1.0/get_tasks', methods=['POST'])
# def change_username():
#     logging.info("Получен запрос на изменение имени пользователя")
#     if 'userid' in request.args:
#         try:
#             userid = request.args['userid']
#             conn = sqlite3.connect('STM.db', check_same_thread=False)
#             cur = conn.cursor()
#             cur.execute("""UPDATE users SET username = 150 WHERE num = 2""")
#         except Exception as e:
#             pass
#         pass


if __name__ == '__main__':
    app.run(debug=True)
