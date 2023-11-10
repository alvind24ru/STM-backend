import logging
import os
import unittest

import werkzeug.security
from flask import Flask, json, request, jsonify
from utils.exceprion_mapper import handler_exception

import appDB
from appDB import init_database
from utils.constants import *
# import dbmethods
import sqlite3
import scripts
from utils.flask import app
import tasks
import users

logging.basicConfig(level=logging.INFO, filename="py_log.log",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("___________________________________Сервер начал работу___________________________________")
app.config['DATABASE_URL'] = DATABASE_PATH

@app.route(f'/test', methods=['GET'])
def test_method():
    return 'True'


if __name__ == '__main__':
    appDB.init_database(app.config.get('DATABASE_URL'))
    try:
        app.run(debug=True, host='0.0.0.0')
    except Exception as e:
        handler_exception(e)



class AbsTest:
    ...







"""
@api {post} /user Создание нового пользователя
@apiName Add User
@apiGroup Пользователи

@apiParam {String} username Уникальное имя пользователя

@apiSuccess UserObject При удачном создании пользователя возвращается созданный User в виде JSON.
@apiSuccessExample {json} Success-Response:
     {
        "userid": 1,
        "username": "name"
    }
@apiError UsernameError Указанное имя пользователя уже используется.
@apiError InvalidArguments Указаны не все аргументы.
"""
# @app.route(f'/api/{VERSION}/users', methods=['POST'])


"""
@api {get} /users/<int:userid> Получение пользователя
@apiName Get User
@apiGroup Пользователи

@apiSuccess UserObject При наличии пользователя с данным id возвращает User в виде JSON.
@apiSuccessExample {json} Success-Response:
     {
        "userid": 1,
        "username": "name"
    }
@apiError UserNotFound Указанный id не найден.
"""
# @app.route(f'/api/{VERSION}/users/<int:userid>', methods=['GET'])
# def get_user(userid):
#     logging.info("Получен запрос на получение пользователя")
#     if dbmethods.user_is_available(userid=userid):
#         try:
#             conn = sqlite3.connect('STM.db', check_same_thread=False)
#             cur = conn.cursor()
#             cur.execute(f"SELECT * FROM users WHERE userid={userid}")
#             result = scripts.list_to_json(cur=cur, data=cur.fetchall())
#             conn.close()
#             return result, 200
#         except Exception as e:
#             logging.critical("Исключение при запросе получения пользователя", exc_info=True)
#             return e, 400
#     else:
#         return 'user not found', 200

"""
@api {update} /users/<int:userid> Обновление пользователя
@apiName Update User
@apiGroup Пользователи

@apiSuccess UserObject При удачном изменении параметров вользователя возвращает объект в виде JSON.
@apiSuccessExample {json} Success-Response:
     {
        "userid": 1,
        "username": "NewName"
    }
@apiError UserNotFound Указанный id не найден.
"""
# @app.route(f'/api/{VERSION}/users/<int:userid>', methods=['UPDATE'])
# def update_user(userid):
#     if 'username' in request.args:
#         try:
#             username = request.args['username']
#             conn = sqlite3.connect('STM.db', check_same_thread=False)
#             cur = conn.cursor()
#             cur.execute(f"""UPDATE users SET username = '{username}' WHERE userid = {userid}""")
#             conn.commit()
#             cur.execute(f"""SELECT * FROM users WHERE userid = {userid}""")
#             result = scripts.list_to_json(cur, cur.fetchall())
#             conn.commit()
#             conn.close()
#             return result, 200, {'Content-Type': 'application/json; charset=utf-8'}
#         except Exception as e:
#             logging.critical("Исключение при попытке изменения пользователя", exc_info=True)
#             return e, 400
#     else:
#         logging.info("Не все необходимые аргументы найдены")
#         return "Invalid argument", 200


"""
@api {delete} /users/<int:userid> Удаление пользователя
@apiName Delete User
@apiGroup Пользователи

@apiSuccess UserObject При удачном удалении возвращает сообщение OK со статусом 200.
@apiError UserNotFound Указанный id не найден.
"""
# @app.route(f'/api/{VERSION}/users/<int:userid>', methods=['DELETE'])
# def delete_user(userid):
#     logging.info("Получен запрос на удаление пользователя")
#     try:
#         if dbmethods.user_is_available(userid=userid):
#             conn = sqlite3.connect('STM.db', check_same_thread=False)
#             cur = conn.cursor()
#             cur.execute(
#                 f"""DELETE FROM users WHERE userid = {userid}""")
#             logging.info(f"Пользователь с ID {userid} удален")
#             conn.commit()
#             conn.close()
#             return 'OK', 200
#         else:
#             return 'there is no user with this id', 200
#     except Exception as e:
#         logging.critical("Исключение при попытке удаления пользователя", exc_info=True)
#         return e, 400

"""
@api {get} /users/all Получение списка пользователей
@apiName Get Users
@apiGroup Пользователи

@apiSuccessExample {json} Success-Response:
     [
    {
        "userid": 1,
        "username": "test12122212212132"
    },
    {
        "userid": 2,
        "username": "test_user"
    },
    {
        "userid": 3,
        "username": "vlad loh"
    },
    {
        "userid": 4,
        "username": "ftest"
    },
    {
        "userid": 5,
        "username": "ftestdddd"
    },
    {
        "userid": 6,
        "username": "ftestddddsd"
    },
    {
        "userid": 7,
        "username": "ftestddddsdsf"
    }
]
"""
# @app.route(f'/api/{VERSION}/users/all', methods=['GET'])
# def get_all_users():
#     logging.info("Получен запрос списка пользователей")
#     try:
#         conn = sqlite3.connect('STM.db', check_same_thread=False)
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM users;")
#         result = scripts.list_to_json(cur, cur.fetchall())
#         conn.close()
#         logging.info("Список пользователей успешно предоставлен")
#         return result, 200, {'Content-Type': 'application/json; charset=utf-8'}
#     except Exception as e:
#         logging.critical("Исключение при запросе списка пользователей", exc_info=True)
#         return e, 400


"""
@api {get} /users/<int:userid>/tasks Получение списка задач для пользователя
@apiName Get user tasks
@apiGroup Задачи


@apiSuccessExample {json} Success-Response:
     [
    {
        "taskid": 4,
        "username": "test_user",
        "title": "test_title22",
        "description": "выпывпывпыв12345поо",
        "done": "FALSE"
    },
    {
        "taskid": 5,
        "username": "test_user",
        "title": "testtttt",
        "description": "выпывпы",
        "done": "FALSE"
    },
    {
        "taskid": 6,
        "username": "test_user",
        "title": "test_title",
        "description": "выпывпывпывпывпывп",
        "done": "FALSE"
    }
     ]
@apiError UserNotFound Указанный id не найден.
"""
# @app.route(f'/api/{VERSION}/users/<int:userid>/tasks', methods=['GET'])
# def get_user_tasks(userid):
#     logging.info("Получен запрос на получение списка задач")
#     try:
#         conn = sqlite3.connect('STM.db', check_same_thread=False)
#         cur = conn.cursor()
#         cur.execute(f"""SELECT username FROM users WHERE userid == {userid}""")
#         username = cur.fetchone()[0]
#         cur.execute(f"""SELECT * FROM tasks WHERE username == '{username}'""")
#         user_tasks_list = scripts.list_to_json(cur, cur.fetchall())
#         logging.info(f"Список задач пользователя {username} предоставлен")
#         conn.commit()
#         conn.close()
#         return user_tasks_list, 200, {'Content-Type': 'application/json; charset=utf-8'}
#     except Exception as e:
#         logging.critical("Исключение при попытке получения задач", exc_info=True)
#         return e, 400


"""
@api {post} /tasks Добавление задачи
@apiName Add Task
@apiGroup Задачи

@apiSuccess UserObject При удачном добавлении задачи возвращает объект в виде JSON.
@apiSuccessExample {json} Success-Response:
    {
    "taskid": 67,
    "username": "ftest",
    "title": "new title",
    "description": "new description",
    "done": "FALSE"
    }
"""

# @app.route(f'/api/{VERSION}/tasks', methods=['POST'])
# def create_task():
#     logging.info("Получен запрос на добавление задачи")
#     if 'username' in request.args and 'title' in request.args and 'description' in request.args and 'done' in request.args:
#         try:
#             username = request.args['username']
#             title = request.args['title']
#             description = request.args['description']
#             done = request.args['done']
#             conn = sqlite3.connect('STM.db', check_same_thread=False)
#             cur = conn.cursor()
#             cur.execute("""SELECT username FROM users""")
#             username_list = cur.fetchall()
#             for i in range(len(username_list)):
#                 if username == username_list[i][0]:
#                     cur.execute(f"""INSERT INTO tasks(username, title, description, done)
#                         VALUES('{username}', '{title}', '{description}', '{done}');""")
#                     conn.commit()
#                     cur.execute(f"""SELECT * FROM tasks WHERE username = '{username}' AND taskid = (SELECT max(taskid)
#                     FROM tasks WHERE username = '{username}')""")
#                     task = scripts.list_to_json(cur, cur.fetchall())
#                     conn.close()
#                     logging.info("Добавлена задача")
#                     return task, 200
#             else:
#                 logging.info("данный username не найден для добавления задачи")
#                 return f"User {username} is not found!"
#         except Exception as e:
#             logging.critical("Исключение при добавлении задачи", exc_info=True)
#             return e, 400
#     else:
#         logging.info("Не все необходимые аргументы найдены")
#         return "Invalid argument", 200


"""
@api {get} /tasks/<int:taskid> Получение задачи
@apiName Get Task
@apiGroup Задачи

@apiSuccessExample {json} Success-Response:
    {
    "taskid": 67,
    "username": "ftest",
    "title": "new title",
    "description": "new description",
    "done": "FALSE"
    }
"""
# @app.route(f'/api/{VERSION}/tasks/<int:taskid>', methods=['GET'])
# def get_task(taskid):
#     try:
#         conn = sqlite3.connect('STM.db', check_same_thread=False)
#         cur = conn.cursor()
#         cur.execute(f"""SELECT * FROM tasks WHERE taskid == {taskid}""")
#         result = scripts.list_to_json(cur, cur.fetchall())
#         conn.commit()
#         conn.close()
#         return result, 200, {'Content-Type': 'application/json; charset=utf-8'}
#     except Exception as e:
#         logging.critical("Исключение при попытке получения задачи", exc_info=True)
#         return e, 400


"""
@api {update} /tasks Обновление задачи
@apiName Update Task
@apiGroup Задачи

@apiSuccess UserObject При удачном обновлении задачи возвращает объект в виде JSON.
@apiSuccessExample {json} Success-Response:
    {
    "taskid": 67,
    "username": "ftest",
    "title": "new title",
    "description": "new description",
    "done": "FALSE"
    }
"""
# @app.route(f'/api/{VERSION}/tasks/<int:taskid>', methods=['UPDATE'])
# def update_tasks(taskid):
#     if 'title' in request.args and 'description' in request.args:
#         try:
#             title = request.args['title']
#             description = request.args['description']
#             conn = sqlite3.connect('STM.db', check_same_thread=False)
#             cur = conn.cursor()
#             cur.execute(f"""UPDATE tasks SET title = '{title}', description = '{description} WHERE taskid = {taskid}""")
#             conn.commit()
#             cur.execute(f"""SELECT * FROM tasks WHERE taskid = {taskid}""")
#             result = scripts.list_to_json(cur, cur.fetchall())
#             conn.commit()
#             conn.close()
#             return result, 200, {'Content-Type': 'application/json; charset=utf-8'}
#         except Exception as e:
#             logging.critical("Исключение при попытке изменения задачи", exc_info=True)
#             return e, 400
#     else:
#         logging.info("Не все необходимые аргументы найдены")
#         return "Invalid argument", 200

"""
@api {delete} /tasks Удаление задачи
@apiName Delete Task
@apiGroup Задачи

@apiSuccessExample {json} Success-Response:
    OK
"""
# @app.route(f'/api/{VERSION}/tasks/<int:taskid>', methods=['DELETE'])
# def delete_task(taskid):
#     logging.info("Получен запрос на удаление задачи")
#     if dbmethods.task_is_available(taskid):
#         try:
#             conn = sqlite3.connect('STM.db', check_same_thread=False)
#             cur = conn.cursor()
#             cur.execute(
#                 f"""DELETE FROM tasks WHERE taskid = {taskid}""")
#             logging.info(f"Задача с ID {taskid} удалена")
#             conn.commit()
#             conn.close()
#             return 'OK', 200
#         except Exception as e:
#             logging.critical("Исключение при попытке удаления задачи", exc_info=True)
#             return e, 400
#     else:
#         return 'there is no task with this id', 200

#
#
#


#
# if __name__ == '__main__':
#     app.run(debug=True)
