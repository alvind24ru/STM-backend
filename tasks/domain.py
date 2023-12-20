from stm_api.tasks.models import Task
from stm_api.tasks.data import TaskDB
from utils.exceptions import *
from stm_api.users.di import domain as user_domain


class TaskDomain:
    """Описывается вся логика"""
    __database: TaskDB

    def __init__(self, database: TaskDB):
        self.__database = database

    def create_task(self, task: Task) -> Task:
        if task.id is None:  # TODO константа noid для обработки ошибок спросить у Ростика емое
            return self.__database.create_task(
                task)  # TODO проверять наличие пользователя (чтобы не создать задачу пользователя, который не существует)
        else:
            raise DomainException('В запросе на создание задачи id не None')

    def get_task(self, taskid: int) -> Task:
        if self.__database.task_is_available(taskid):
            return self.__database.get_task(taskid)
        else:
            raise DomainException("Задачи с таким ID не существует")

    def update_tasks(self, task: Task) -> Task:
        if self.__database.task_is_available(task.id):
            return self.__database.update_task(task)
        else:
            raise DomainException('Задачи с таким ID не существует')

    def delete_tasks(self, taskid: int):
        if self.__database.task_is_available(taskid):
            result = self.__database.delete_task(taskid)
            if result:
                return str(result)
        else:
            raise DomainException('Нет удаляемой задачи')

    def get_all_user_tasks(self, userid: int) -> list:
        username = user_domain.get_user(userid).username
        return self.__database.get_all_user_tasks(username)
