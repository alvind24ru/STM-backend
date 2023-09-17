from users.data import UsersDB
from users.models import User
from utils.exceptions import UserException


class UsersDomain:
    __database: UsersDB

    def __init__(self, database: UsersDB):
        self.__database = database

    def create_user(self, user: User):
        return self.__database.create_user(user)

    def get_user(self, userid: int) -> User:
        if self.__database.user_is_available(userid):
            return self.__database.get_user(userid)
        else:
            raise UserException('Нет запрашиваемого пользователя')

    def update_user(self, user: User) -> User:
        if self.__database.user_is_available(user.userid):
            return self.__database.update_user(user)
        else:
            raise UserException('Нет обновляемого пользователя')

    def delete_user(self, userid):
        if self.__database.user_is_available(userid):
            return self.__database.delete_user(userid)
        else:
            raise UserException('Нет удаляемого пользователя')

    def get_all_users(self):
        print('domain')
        return self.__database.get_all_users()
