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
            cur.execute(f"""INSERT INTO users(username) VALUES('{user.username}')""")
            conn.commit()
            cur.execute(f"SELECT * FROM users WHERE username='{user.username}'")
            db_result = cur.fetchall()
            conn.close()
            logging.log_info(f'Выполнено создание пользователя {user.username}')
            return self.__list_to_object(db_result[0])
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
            logging.log_info(f'Выполнен запрос на получение пользователя c id {userid}')
            return self.__list_to_object(db_result[0])
        except Exception as ex:
            raise DBException(ex, f"Исключение при получении пользователя c id {userid}")

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
            return self.__list_to_object(db_result[0])
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
            logging.log_info(f'Получен список всех пользователей: {data}')
            for i in data:
                res.append(self.__list_to_object(i))
            return res
        except Exception as ex:
            raise DBException(ex, f"Исключение в БД при получении всех пользователей")

    @staticmethod
    def __list_to_object(data: list) -> User:
        """Преобразует входные данные вида list в объект User"""
        logging.log_info(f'Преобразование в объект данных: {data}, {type(data)}')
        user = User()
        user.userid = data[0]
        user.username = data[1]
        logging.log_info(f'Преобразованные данные: {user}')
        return user
