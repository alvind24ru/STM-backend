from stm_api.users.data import UsersDB
from stm_api.users.models import User
from utils.exceptions import DomainException


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
            raise DomainException('Нет запрашиваемого пользователя')

    def update_user(self, user: User) -> User:
        if self.__database.user_is_available(user.userid):
            return self.__database.update_user(user)
        else:
            raise DomainException('Нет обновляемого пользователя')

    def delete_user(self, userid):
        if self.__database.user_is_available(userid):
            return self.__database.delete_user(userid)
        else:
            raise DomainException('Нет удаляемого пользователя')

    def get_all_users(self):
        return self.__database.get_all_users()

    def check_user_id_or_except(self, userid: int):
        if self.__database.user_is_available(userid):
            return
        else:
            raise DomainException(f'Пользователя c {userid} не существует')
