from users.domain import UsersDomain
from users.models import User
from utils.exceptions import ViewException
from utils import logging_util as logging

USERID = 'userid'
USERNAME = 'username'


class UserPresentation:
    __domain: UsersDomain

    def __init__(self, domain: UsersDomain):
        self.__domain = domain

    def create_user(self, args) -> str:
        if USERNAME in args:
            return self.__user_to_json(self.__domain.create_user(User(userid=None, username=args['username'])))
        else:
            raise ViewException("Отсутствуют необходимые аргументы")

    def get_user(self, userid: int) -> str:
        if userid:
            return self.__user_to_json(self.__domain.get_user(userid))
        else:
            raise ViewException("Отсутствуют необходимые аргументы")

    def update_user(self, args) -> str:
        if USERNAME and USERID in args:
            return self.__user_to_json(self.__domain.update_user(self.__args_to_user_object(args)))
        else:
            raise ViewException("Отсутствуют необходимые аргументы")

    def delete_user(self, userid: int) -> str:
        if userid:
            return str(self.__domain.delete_user(userid))
        else:
            raise ViewException("Отсутствуют необходимые аргументы")

    def get_all_users(self) -> str:
        data = self.__domain.get_all_users()
        res = "["
        for i in data:
            res += self.__user_to_json(i)
            if i != data[-1]:
                res += ','
        res += ']'
        return res

    @staticmethod
    def __args_to_user_object(args) -> User:
        return User(userid=args['userid'], username=args['username'])

    @staticmethod
    def __user_to_json(user: User) -> str:
        return f"""{{"{USERID}": {user.userid},
        "{USERNAME}": "{user.username}"}}"""
