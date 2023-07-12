import logging
from flask import Flask, json, request, jsonify

import DBoperators
from DBoperators import *
import sqlite3
import scripts

# TODO Найти нормальную библиотеку для сериализации данных из БД в JSON
with open('apidoc.json') as file:
    data = json.load(file)

VERSION = 'v' + data['version']

logging.basicConfig(level=logging.INFO, filename="py_log.log",
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


@app.route(f'/api/{VERSION}/users/create', methods=['POST'])
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
            cur.execute(f"SELECT * FROM users WHERE username='{username}'")
            created_user = scripts.list_to_json(cur=cur, data=cur.fetchall())
            conn.close()
            return created_user, 200
        except sqlite3.IntegrityError:
            logging.error("Указанное имя пользователя уже имеется", exc_info=True)
            return 'the username is already in use', 200
        except Exception as e:
            logging.critical("Исключение при запросе на добавление пользователя", exc_info=True)
            return e, 400
    else:
        logging.info("Не все необходимые аргументы найдены")
        return "InvalidArguments", 200


@app.route(f'/api/{VERSION}/users/get/<string:username>', methods=['GET'])
def get_user(username):
    logging.info("Получен запрос на получение пользователя")
    if DBoperators.user_is_available(username=username):
        try:
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM users WHERE username='{username}'")
            result = scripts.list_to_json(cur=cur, data=cur.fetchall())
            conn.close()
            return result, 200
        except Exception as e:
            logging.critical("Исключение при запросе получения пользователя", exc_info=True)
            return e, 400
    else:
        return 'user not found', 200


@app.route(f'/api/{VERSION}/users/update', methods=['POST'])
def update_user():
    if 'userid' in request.args and 'username' in request.args:
        try:
            userid = request.args['userid']
            username = request.args['username']
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""UPDATE users SET username = '{username}' WHERE userid = {userid}""")
            conn.commit()
            cur.execute(f"""SELECT * FROM users WHERE userid = {userid}""")
            result = scripts.list_to_json(cur, cur.fetchall())
            conn.commit()
            conn.close()
            return result, 200, {'Content-Type': 'application/json; charset=utf-8'}
        except Exception as e:
            logging.critical("Исключение при попытке изменения пользователя", exc_info=True)
            return e, 400
    else:
        logging.info("Не все необходимые аргументы найдены")
        return "Invalid argument", 200


@app.route(f'/api/{VERSION}/users/delete/<int:userid>', methods=['GET'])
def delete_user(userid):
    logging.info("Получен запрос на удаление пользователя")
    try:
        if DBoperators.user_is_available(userid=userid):
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute(
                f"""DELETE FROM users WHERE userid = {userid}""")
            logging.info(f"Пользователь с ID {userid} удален")
            conn.commit()
            conn.close()
            return 'OK', 200
        else:
            return 'there is no user with this id', 200
    except Exception as e:
        logging.critical("Исключение при попытке удаления пользователя", exc_info=True)
        return e, 400


@app.route(f'/api/{VERSION}/users/get/all', methods=['GET'])
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
    except Exception as e:
        logging.critical("Исключение при запросе списка пользователей", exc_info=True)
        return e, 400


@app.route(f'/api/{VERSION}/tasks/create', methods=['POST'])
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
                    cur.execute(f"""SELECT * FROM tasks WHERE username = '{username}' AND taskid = (SELECT max(taskid) 
                    FROM tasks WHERE username = '{username}')""")
                    task = scripts.list_to_json(cur, cur.fetchall())
                    conn.close()
                    logging.info("Добавлена задача")
                    return task, 200
            else:
                logging.info("данный username не найден для добавления задачи")
                return f"User {username} is not found!"
        except Exception as e:
            logging.critical("Исключение при добавлении задачи", exc_info=True)
            return e, 400
    else:
        logging.info("Не все необходимые аргументы найдены")
        return "Invalid argument", 200


@app.route(f'/api/{VERSION}/tasks/get-all/<int:userid>', methods=['GET'])
def get_all_user_tasks(userid):
    logging.info("Получен запрос на получение списка задач")
    try:
        conn = sqlite3.connect('STM.db', check_same_thread=False)
        cur = conn.cursor()
        cur.execute(f"""SELECT username FROM users WHERE userid == {userid}""")
        username = cur.fetchone()[0]
        cur.execute(f"""SELECT * FROM tasks WHERE username == '{username}'""")
        user_tasks_list = scripts.list_to_json(cur, cur.fetchall())
        logging.info(f"Список задач пользователя {username} предоставлен")
        conn.commit()
        conn.close()
        return user_tasks_list, 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        logging.critical("Исключение при попытке получения задач", exc_info=True)
        return e, 400


@app.route(f'/api/{VERSION}/tasks/get/<int:taskid>', methods=['GET'])
def get_task(taskid):
    try:
        conn = sqlite3.connect('STM.db', check_same_thread=False)
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM tasks WHERE taskid == {taskid}""")
        result = scripts.list_to_json(cur, cur.fetchall())
        conn.commit()
        conn.close()
        return result, 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        logging.critical("Исключение при попытке получения задачи", exc_info=True)
        return e, 400


@app.route(f'/api/{VERSION}/tasks/update', methods=['POST'])
def update_tasks():
    if 'taskid' in request.args and 'title' in request.args and 'description' in request.args:
        try:
            taskid = request.args['taskid']
            title = request.args['title']
            description = request.args['description']
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""UPDATE tasks SET title = '{title}' WHERE taskid = {taskid}""")
            cur.execute(f"""UPDATE tasks SET description = '{description}' WHERE taskid = {taskid}""")
            conn.commit()
            cur.execute(f"""SELECT * FROM tasks WHERE taskid = {taskid}""")
            result = scripts.list_to_json(cur, cur.fetchall())
            conn.commit()
            conn.close()
            return result, 200, {'Content-Type': 'application/json; charset=utf-8'}
        except Exception as e:
            logging.critical("Исключение при попытке изменения задачи", exc_info=True)
            return e, 400
    else:
        logging.info("Не все необходимые аргументы найдены")
        return "Invalid argument", 200


@app.route(f'/api/{VERSION}/tasks/delete/<int:taskid>', methods=['GET'])
def delete_task(taskid):
    logging.info("Получен запрос на удаление задачи")
    if DBoperators.task_is_available(taskid):
        try:
            conn = sqlite3.connect('STM.db', check_same_thread=False)
            cur = conn.cursor()
            cur.execute(
                f"""DELETE FROM tasks WHERE taskid = {taskid}""")
            logging.info(f"Задача с ID {taskid} удалена")
            conn.commit()
            conn.close()
            return 'OK', 200
        except Exception as e:
            logging.critical("Исключение при попытке удаления задачи", exc_info=True)
            return e, 400
    else:
        return 'there is no task with this id', 200

@app.route('/test', methods=['GET'])
def test():
    return 'True'


if __name__ == '__main__':
    app.run(debug=True)
