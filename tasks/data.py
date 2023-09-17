import sqlite3

from tasks.models import Task
from utils import logging_util as logging
from utils.exceptions import *


class TaskDB:
    __db_name: str

    def __init__(self, db_name: str):
        self.__db_name = db_name

    def create_task(self, task: Task) -> Task:
        try:
            conn = sqlite3.connect(self.__db_name, check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO tasks (username, title, description, done) 
                VALUES('{task.username}', '{task.title}', '{task.description}', '{task.done}');""")
            conn.commit()  # TODO найти как сразу получать созданную таску
            cur.execute(f"""SELECT * FROM tasks WHERE username = '{task.username}' AND taskid = (SELECT max(taskid)
            FROM tasks WHERE username = '{task.username}')""")
            db_result = cur.fetchall()
            conn.close()
            logging.log_info(f"Пользователю {task.username} добавлена задача c идентификатором {task.id}")
            return self.__read_task(db_result)
        except Exception as ex:
            raise DBException(ex, f"Исключение при попытке создания задачи с id {task.id} пользователя {task.username}")

    def get_task(self, taskid: int) -> Task:
        try:
            conn = sqlite3.connect(self.__db_name, check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""SELECT * FROM tasks WHERE taskid == {taskid}""")
            db_result = cur.fetchall()
            conn.close()
            logging.log_info(f"Выполнен запрос на задачу с id {taskid}")
            return self.__read_task(db_result)
        except Exception as ex:
            raise DBException(ex, f"Исключение при попытке получения задачи с id {taskid}")

    def update_task(self, task: Task) -> Task:
        try:
            conn = sqlite3.connect(self.__db_name, check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""UPDATE tasks SET 
                        username = {task.username},
                        title = {task.title},
                        description = {task.description},
                        done = {task.done} WHERE taskid = {task.id}""")
            conn.commit()
            conn.close()
            logging.log_info(f"Выполнено обновление задачи с id {task.id}")
            return self.get_task(task.id)
        except Exception as ex:
            raise DBException(ex,
                              f"Исключение при попытке обновления задачи с id {task.id} пользователя {task.username}")

    def delete_task(self, taskid: int) -> bool:
        try:
            conn = sqlite3.connect(self.__db_name, check_same_thread=False)
            cur = conn.cursor()
            cur.execute(
                f"""DELETE FROM tasks WHERE taskid = {taskid}""")
            conn.commit()
            conn.close()
            logging.log_info(f"Выполнено удаление задачи с id {taskid}")
            return True
        except Exception as ex:
            raise DBException(ex, f"Исключение при попытке удаления задачи с id {taskid}")

    def task_is_available(self, taskid: int) -> bool:
        conn = sqlite3.connect(self.__db_name, check_same_thread=False)
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM tasks WHERE taskid = {taskid}""")
        res = cur.fetchall()
        conn.close()
        if res:
            return True
        else:
            return False

    @staticmethod  # TODO разобраться в статикметодах и классметодАХ
    def __read_task(data: list) -> Task:
        """Преобразует входные данные вида list в объект Task"""
        task = Task()
        task.id = data[0][0]
        task.username = data[0][1]
        task.title = data[0][2]
        task.description = data[0][3]
        task.done = data[0][4]
        return task
