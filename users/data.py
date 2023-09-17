import sqlite3

from users.models import User
from utils import logging_util as logging
from utils.exceptions import *


class UsersDB:
    __db_name: str

    def __init__(self, db_name: str):
        self.__db_name = db_name

    def create_user(self, user: User) -> User:
        try:
            conn = sqlite3.connect(self.__db_name, check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO users(username) VALUES('{User.username}')""")
            conn.commit()
            cur.execute(f"SELECT * FROM users WHERE username='{User.username}'")
            db_result = cur.fetchall()
            conn.close()
            logging.log_info(f'Выполнено создание пользователя {user.username}')
            return self.__read_user(db_result)
        except Exception as ex:
            raise DBException(ex,
                              f"Исключение при попытке создания пользователя с id {user.userid} и именем {user.username}")

    def get_user(self, userid: int) -> User:
        try:
            conn = sqlite3.connect(self.__db_name, check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM users WHERE userid={userid}")
            db_result = cur.fetchall()
            conn.close()
            logging.log_info(f'Выполнен запрос на получение пользователя {userid}')
            return self.__read_user(db_result)
        except Exception as ex:
            raise DBException(ex, f"Исключение при получении пользователя {userid}")

    def update_user(self, user: User) -> User:
        try:
            conn = sqlite3.connect(self.__db_name, check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""UPDATE users SET username = '{user.username}' WHERE userid = {user.userid}""")
            conn.commit()
            cur.execute(f"""SELECT * FROM users WHERE userid = {user.userid}""")
            db_result = cur.fetchall()
            conn.close()
            logging.log_info(f'Выполнено обновление пользователя {user.username}')
            return self.__read_user(db_result)
        except Exception as ex:
            raise DBException(ex, f"Исключение при обновлении пользователя {user.username}")

    def delete_user(self, userid: int) -> bool:
        try:
            conn = sqlite3.connect(self.__db_name, check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""DELETE FROM users WHERE userid = {userid}""")
            conn.commit()
            conn.close()
            logging.log_info(f'Выполнено удаление пользователя с id {userid}')
            return True
        except Exception as ex:
            raise DBException(ex, f"Исключение при удалении пользователя с id {userid}")

    def user_is_available(self, userid: int) -> bool:
        conn = sqlite3.connect(self.__db_name, check_same_thread=False)
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM users WHERE userid = {userid}""")
        res = cur.fetchall()
        conn.close()
        if res:
            return True
        else:
            return False

    def get_all_users(self):
        try:
            conn = sqlite3.connect(self.__db_name, check_same_thread=False)
            cur = conn.cursor()
            cur.execute(f"""SELECT * FROM users""")
            data = cur.fetchall()
            conn.commit()
            conn.close()
            logging.log_info(f'Выполнен запрос на получение всех пользователей')
            res = []
            for i in data:
                res.append(self.__read_user(i))
            print('database')
            return res
        except Exception as ex:
            raise DBException(ex, f"Исключение при получении всех пользователей")

    @staticmethod
    def __read_user(data: list) -> User:
        """Преобразует входные данные вида list в объект User"""
        user = User()
        user.id = data[0][0]
        user.username = data[0][1]
        user.title = data[0][2]
        user.description = data[0][3]
        user.done = data[0][4]
        return user
